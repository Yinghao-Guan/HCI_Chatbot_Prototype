from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # 允许跨域请求

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:1.5b"  #

# 全局对话历史
conversation_history = []


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # 记录用户输入
    conversation_history.append({"role": "user", "content": user_input})

    # 将历史拼接成 prompt
    full_prompt = ""
    for msg in conversation_history:
        prefix = "User:" if msg["role"] == "user" else "AI:"
        full_prompt += f"{prefix} {msg['content']}\n"
    full_prompt += "AI:"  # 提示模型继续回答

    # --- 流式响应逻辑 ---

    def generate_stream():
        """
        这是一个生成器函数，它将流式传输来自 Ollama 的响应。
        """
        # 用于在流结束后保存完整响应
        full_ai_reply = ""

        try:
            # 调用 Ollama，关键：stream=True
            response = requests.post(
                OLLAMA_API_URL,
                json={
                    "model": MODEL_NAME,  #
                    "prompt": full_prompt,
                    "stream": True
                },
                stream=True  # 告诉 requests 库保持连接打开
            )
            response.raise_for_status()  # 如果请求失败（如 404, 500），则引发异常

            # Ollama 的流式响应是每行一个 JSON 对象
            for line in response.iter_lines():
                if line:
                    try:
                        # 解码行（它是 bytes 类型）
                        json_line = line.decode('utf-8')
                        # 解析 JSON
                        data = json.loads(json_line)

                        # "response" 键包含文本块
                        text_chunk = data.get("response", "")

                        if text_chunk:
                            full_ai_reply += text_chunk
                            # `yield` (产出) 文本块，这会立即发送给前端
                            yield text_chunk.encode('utf-8')  # 确保以 bytes 形式发送

                        # Ollama 在流结束时会发送一个 "done": true 的最终对象
                        if data.get("done", False):
                            break

                    except json.JSONDecodeError:
                        print(f"Warning：Unable to decode JSON on row: {line}")
                        pass  # 忽略无效的 JSON 行

        except requests.RequestException as e:
            print(f"Error: Failed connecting Ollama: {e}")
            yield f"⚠️ Failed connecting backend LLM: {e}".encode('utf-8')
        finally:
            # --- 流式传输结束后 ---
            # 将完整的 AI 回复保存到历史记录中
            if full_ai_reply:
                conversation_history.append({"role": "ai", "content": full_ai_reply.strip()})
            print("Streaming Complete")

    # 返回一个 Flask Response 对象，内容是我们的生成器
    # mimetype='text/plain' 告诉浏览器这是一个纯文本流
    return Response(generate_stream(), mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True)  #