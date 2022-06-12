import os
from flask import Flask
import Constants as keys
from telegram.ext import *
import Responses as R

app = Flask(__name__)


print("Bot started...")

def start_command(update, context):
    update.message.reply_text("How may we help today?")


def help_command(update, context):
    update.message.reply_text("If you need help. Please ... ")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

@app.route("/")
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))