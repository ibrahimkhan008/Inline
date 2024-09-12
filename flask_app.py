from flask import Flask, request
import telegram
from inline import Updater  # Import the 'updater' object from inline.py

# Initialize Flask app
app = Flask(__name__)

# Use the bot from inline.py
bot = Updater.bot  # This uses the already initialized bot in inline.py

@app.route('/', methods=['GET'])
def home():
    return "Telegram Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    # Process the update with inline.py's dispatcher
    Updater.dispatcher.process_update(update)
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
