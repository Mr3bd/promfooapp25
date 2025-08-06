from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_prompt = data.get("prompt", "Hello! How can I help you?")
    if not user_prompt:
        return jsonify({"error": "Missing 'prompt' in request."}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.7,
        )
        message = response.choices[0].message.content.strip()
        return jsonify({"response": message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)
