from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:1.5b"

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

    # 调用 Ollama
    response = requests.post(OLLAMA_API_URL, json={
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    })

    if response.status_code != 200:
        return jsonify({"error": "Ollama request failed"}), 500

    ai_reply = response.json().get("response", "")
    conversation_history.append({"role": "ai", "content": ai_reply})

    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    app.run(debug=True)
