from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv(8145456331:AAHUtwqnbWt7zU1DcjuCasYe0nbY2orngYI)

def start(update, context):
    update.message.reply_text("✅ ربات فعال شد!")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
