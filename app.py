from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is running!"


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    return "Webhook received!", 200

if __name__ == '__main__':
    app.run(debug=True)
