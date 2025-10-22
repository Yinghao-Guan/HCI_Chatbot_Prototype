from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
import os
import json
import time

from backend import llm_service
from backend import data_manager
from backend.config import VERSION_MAP, EXPERIMENT_STEPS

# --- Flask App Setup ---
project_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(project_root)
app = Flask(__name__, static_folder=project_root)
CORS(app)

data_manager.create_data_dir()


# --- 辅助函数：计算简单文本指标 ---
def calculate_text_metrics(text: str) -> dict:
    """计算字符数、词数和模拟的 token 数"""
    text = text.strip()
    char_count = len(text)
    word_count = len(text.split())
    # 模拟 token 计数: 假设一个字符平均 1/3 个 token
    token_count = max(1, int(char_count / 3))

    return {
        "length_char": char_count,
        "length_word": word_count,
        "length_token": token_count
    }


# --- 静态文件服务路由 (保持不变) ---

@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/html/<path:filename>')
def serve_html(filename):
    return send_from_directory(os.path.join(app.static_folder, 'html'), filename)


@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(os.path.join(app.static_folder, 'assets'), filename)


# --- 实验初始化路由 (保持不变) ---

@app.route('/start_experiment', methods=['POST'])
def start_experiment():
    try:
        data = request.json
        participant_id = data.get("participant_id")
        condition = data.get("condition")

        if not participant_id or not condition:
            return jsonify({"error": "Missing participant_id or condition"}), 400

        llm_service.clear_session(participant_id)

        # 初始化数据并获取下一步 URL (Demographics)
        next_url = data_manager.init_participant_session(participant_id, condition)

        return jsonify({"success": True, "next_url": next_url})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Error in /start_experiment: {e}")
        return jsonify({"error": f"Internal server error: {e}"}), 500


# --- 通用数据保存与流程控制路由 (保持不变) ---

@app.route('/save_data', methods=['POST'])
def save_data():
    try:
        data = request.json
        participant_id = data.get("participant_id")
        step_name = data.get("step_name")
        step_data = data.get("data")
        current_step_index = data.get("current_step_index")

        if not participant_id or not step_name or step_data is None or current_step_index is None:
            return jsonify({"error": "Missing required fields"}), 400

        # 1. 保存当前步骤的数据
        data_manager.save_participant_data(participant_id, step_name, step_data)

        # 2. 确定下一个页面的 URL (流程控制)
        next_step_index = current_step_index + 1

        if next_step_index >= len(EXPERIMENT_STEPS):
            next_url = "/html/debrief.html"
        else:
            next_step_key = EXPERIMENT_STEPS[next_step_index]

            if next_step_key == "DIALOGUE":
                # 特殊处理：获取实验条件对应的聊天页面 URL
                status = data_manager.get_participant_status(participant_id)
                condition = status.get("condition", "NON_XAI")
                next_url = VERSION_MAP.get(condition, VERSION_MAP["NON_XAI"])
            else:
                next_url = f"/html/{next_step_key.lower()}.html"

        return jsonify({"success": True, "next_url": next_url})

    except Exception as e:
        print(f"Error in /save_data: {e}")
        return jsonify({"error": f"Internal server error: {e}"}), 500


# --- 聊天交互路由 (核心修改：只记录指标) ---

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    participant_id = request.json.get("participant_id", "")
    # 从前端接收 XAI 解释是否显示的状态 (在 XAI 版本中为 True/False)
    explanation_shown = request.json.get("explanation_shown", False)

    if not user_input or not participant_id:
        return Response("⚠️ No message or participant_id provided", status=400, mimetype='text/plain')

    session = llm_service.get_session(participant_id)
    condition = data_manager.get_participant_condition(participant_id)

    # 在流开始前记录回合数（LLM Service 内部会+1）
    current_turn = session['turn_count'] + 1
    user_metrics = calculate_text_metrics(user_input)

    def generate_stream_and_log():
        full_ai_reply = b''

        # 1. 调用 LLM 服务生成流
        stream = llm_service.get_llm_response_stream(participant_id, user_input)

        for chunk in stream:
            full_ai_reply += chunk
            yield chunk

        # 2. 在流结束后，记录回合分析数据 (如果 LLM 成功回复且回合数增加)
        if full_ai_reply and session['turn_count'] == current_turn:
            # 从 session history 获取最新的 AI 消息 (确保它已经被 llm_service 规范化处理)
            ai_message = session['history'][-1]['content']
            agent_metrics = calculate_text_metrics(ai_message)

            turn_data = {
                "user_id": participant_id,
                "condition": condition,
                "turn": current_turn,

                # 用户指标 (情感占位符)
                "user_sentiment_score": None,
                "user_sentiment_label": None,
                "user_input_length_token": user_metrics["length_token"],
                "user_input_length_char": user_metrics["length_char"],
                "user_input_length_word": user_metrics["length_word"],

                # Agent 指标 (情感占位符)
                "agent_sentiment_score": None,
                "agent_sentiment_label": None,
                "agent_response_length_token": agent_metrics["length_token"],
                "agent_response_length_char": agent_metrics["length_char"],
                "agent_response_length_word": agent_metrics["length_word"],

                # XAI 状态
                "explanation_shown": explanation_shown if condition == "XAI" else False
            }

            # 3. 存储回合分析数据
            data_manager.save_turn_data(participant_id, turn_data)

    return Response(generate_stream_and_log(), mimetype='text/plain')


# --- 新增路由：保存对话结束指标 (如情绪波动) ---

@app.route('/save_dialogue_end_metrics', methods=['POST'])
def save_dialogue_end_metrics():
    """用于在对话结束后保存最终指标（如情绪波动），并控制流程跳转。"""
    try:
        data = request.json
        participant_id = data.get("participant_id")

        if not participant_id:
            return jsonify({"error": "Missing participant_id"}), 400

        # --- TODO: 情绪波动计算的占位符 ---
        # 假设情绪得分列表为 session['sentiment_scores']，但目前为空或为 None
        # 实际计算: max(scores) - min(scores)
        emotion_fluctuation_value = 0.0

        session = llm_service.get_session(participant_id)

        end_data = {
            "emotion_fluctuation": emotion_fluctuation_value,
            "total_turns": session['turn_count']
        }

        # 保存对话结束数据
        data_manager.save_participant_data(participant_id, "DIALOGUE_END", end_data)

        # 流程控制：跳转到 Post-questionnaire 页面
        # DIALOGUE 步骤的下一个是 POST_QUESTIONNAIRE
        next_step_index = EXPERIMENT_STEPS.index("DIALOGUE") + 1
        next_step_key = EXPERIMENT_STEPS[next_step_index]
        next_url = f"/html/{next_step_key.lower()}.html"

        return jsonify({"success": True, "next_url": next_url})

    except Exception as e:
        print(f"Error in /save_dialogue_end_metrics: {e}")
        return jsonify({"error": f"Internal server error: {e}"}), 500


# --- 运行 Flask 服务器 ---
if __name__ == "__main__":
    print("🚀 Starting Flask server on http://127.0.0.1:5000")
    print(f"💾 Data will be saved to: {data_manager.DATA_DIR}")
    app.run(debug=True, port=5000)