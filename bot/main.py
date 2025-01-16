# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import telegram
# # Botni yaratish
# bot = telegram.Bot(token='7725923661:AAEwEvqw7V6icuD2t9f7jTiK_LfdD-AaMV8')
from telegram.ext import Updater

# /start komandasini bajaruvchi funksiya
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id  # chat_id ni update orqali olish
    bot.send_message(chat_id=chat_id, text=f"Hello {chat_id}")


# Botni ishga tushurish
def main():
    # Updater orqali botni ishga tushurish
    updater = Updater('7725923661:AAEwEvqw7V6icuD2t9f7jTiK_LfdD-AaMV8', use_context=True)

    # Dispatcher orqali handler qo'shish
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Botni ishga tushurish
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
