import requests
from flask import Flask, request

# Bot Token
BOT_TOKEN = "7850180113:AAH1Bzj7wXnbbZd4BFVuVbppx4PxzWlQ134"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

# Source & Destination Chat IDs
SOURCE_CHAT_ID = "@Jp_Loot_Deals"  # Yahan source channel ka username likhein
DESTINATION_CHAT_ID = "@ekconverter20bot"  # Yahan destination bot ya group ka username likhein

# Flask App (Cloud Hosting ke liye)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json()
    if "message" in update:
        message = update["message"]
        if "message_id" in message:
            forward_message(message["message_id"])
    return {"ok": True}

def forward_message(message_id):
    url = f"{BASE_URL}/forwardMessage"
    data = {
        "chat_id": DESTINATION_CHAT_ID,
        "from_chat_id": SOURCE_CHAT_ID,
        "message_id": message_id
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
  
