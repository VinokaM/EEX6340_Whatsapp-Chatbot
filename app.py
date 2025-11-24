from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

from Whatsapp.sendMessage import send_whatsapp_message

load_dotenv()

app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
VERIFY_TOKEN    = os.getenv('VERIFY_TOKEN')

def get_llama_response(user_message):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful customer support chatbot."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)
    response_json = response.json()

    return response_json["choices"][0]["message"]["content"]

@app.route("/chat", methods=["GET"])
def verify():
    if request.args.get("hub.mode") == "subscribe" \
       and request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed", 403

# Endpoint to receive messages (later from WhatsApp)
@app.route("/chat", methods=["POST"])
def chat():
    incoming_data = request.json

    try:
        changes = incoming_data["entry"][0]["changes"][0]["value"]
        messages = changes.get("messages")
        if not messages or len(messages) == 0:
            
            return jsonify({"status": "ignored", "reason": "No message received"}), 200

        message = messages[0]
        message_id = message["id"]
        user_message = message["text"]["body"]
        phone_number = message["from"]

    except (KeyError, IndexError):
        return jsonify({"status": "ignored", "reason": "Non-message webhook"}), 200
    
    print(f"User Messge Received from webhook : {user_message}")

    data = request.get_json()

    user_msg = data.get("message")

    bot_reply = get_llama_response(user_message)

    # return jsonify({"reply": bot_reply})
    return send_whatsapp_message(phone_number, bot_reply)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
