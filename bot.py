from telegram.ext import Updater, CommandHandler

def start(update, context,):
    update.message.reply_text("Hola, fotito")

if __name__ == "__main__":
    updater = Updater(token="5180778498:AAERnwryQjpwk5w_pLoHD4F5ONk5KMuyOMM", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle

