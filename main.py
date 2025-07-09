import requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# === BOT TOKEN ===
TOKEN = "7648391331:AAGCbiIx_sD_ZsF3VoNwzvkD-IWxeQp4uG4"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("⚽ Yo! I'm Phantomz_Bot — your AI football prediction homie. Type /predict team1 vs team2")

def predict(update: Update, context: CallbackContext):
    try:
        query = ' '.join(context.args)
        team1, team2 = [t.strip() for t in query.split("vs")]

        response = f"🔮 Predicting {team1} vs {team2}...\n"
        response += f"{team1} win chance: 47%\n"
        response += f"{team2} win chance: 41%\n"
        response += f"Draw: 12%\n\n⚡ (Prediction logic upgrade coming soon...)"
        update.message.reply_text(response)
    except:
        update.message.reply_text("Bruh, type it like: /predict Arsenal vs Chelsea")

def help_command(update: Update, context: CallbackContext):
    commands = """
📘 *Phantomz Commands*
/start - Intro
/predict team1 vs team2 - Predict a match
/help - Show commands
    """
    update.message.reply_text(commands, parse_mode='Markdown')

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("predict", predict))
    dp.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
