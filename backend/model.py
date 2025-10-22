from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:1.5b"

# === 全局存储 ===
conversation_history = []
summary_memory = ""  # summary memory
SUMMARY_INTERVAL = 5  # generate summary every 5 rounds

# === System prompt (only once at the start) ===
SYSTEM_PROMPT = (
    "You are a gentle and empathetic conversational partner. "
    "Always respond in a natural, human-like manner. "
    "Keep your responses consistent with the user's language. "
    "Do not comment on the user's language skills."
)

#     "Understand both English and Chinese input, but when replying in English, "

# === Helper function ===
def generate_summary():
    """Generate a brief summary of recent dialogue (mainly for context memory)"""
    global summary_memory

    recent_dialogue = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in conversation_history[-10:]]
    )

    summary_prompt = f"""
Please summarize the following conversation into a concise summary of no more than 150 words. 
Focus on the user's main emotions, topics, and intents. Keep the summary in English.

Previous summary (if any):
{summary_memory if summary_memory else "(None)"}

New conversation:
{recent_dialogue}

Output the new summary:
"""

    try:
        resp = requests.post(
            OLLAMA_API_URL,
            json={
                "model": MODEL_NAME,
                "prompt": summary_prompt,
                "stream": False
            },
            timeout=120
        )
        data = resp.json()
        new_summary = data.get("response", "").strip()
        if new_summary:
            summary_memory = new_summary
            print("✅ [Summary Updated]:", summary_memory)
    except Exception as e:
        print(f"⚠️ Failed to generate summary: {e}")


# === Main chat endpoint ===
@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history, summary_memory

    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    conversation_history.append({"role": "user", "content": user_input})

    # --- Build prompt ---
    full_prompt = ""

    # Add system prompt only at the start
    if len(conversation_history) == 1:
        full_prompt += SYSTEM_PROMPT + "\n\n"

    # Add summary memory if exists
    if summary_memory:
        full_prompt += f"The following is a summary of previous conversation to help you understand context:\n{summary_memory}\n\n"

    # Add recent conversation (last 10 messages)
    for msg in conversation_history[-10:]:
        prefix = "User:" if msg["role"] == "user" else "AI:"
        full_prompt += f"{prefix} {msg['content']}\n"

    full_prompt += "AI:"

    print(full_prompt)

    # --- Stream response ---
    def generate_stream():
        full_ai_reply = ""
        try:
            response = requests.post(
                OLLAMA_API_URL,
                json={
                    "model": MODEL_NAME,
                    "prompt": full_prompt,
                    "stream": True
                },
                stream=True
            )
            response.raise_for_status()

            for line in response.iter_lines():
                if line:
                    try:
                        json_line = line.decode('utf-8')
                        data = json.loads(json_line)
                        text_chunk = data.get("response", "")
                        if text_chunk:
                            full_ai_reply += text_chunk
                            yield text_chunk.encode('utf-8')
                        if data.get("done", False):
                            break
                    except json.JSONDecodeError:
                        pass

        except requests.RequestException as e:
            yield f"⚠️ Failed connecting backend LLM: {e}".encode('utf-8')

        finally:
            if full_ai_reply:
                conversation_history.append({"role": "ai", "content": full_ai_reply.strip()})
                if len(conversation_history) % (SUMMARY_INTERVAL * 2) == 0:
                    generate_summary()
            print("✅ Streaming Complete")

    return Response(generate_stream(), mimetype='text/plain')


# === Run Flask server ===
if __name__ == "__main__":
    app.run(debug=True)
