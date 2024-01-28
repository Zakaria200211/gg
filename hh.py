import cv2
from deepart import deepart
from telegram import Bot
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters
from telegram.ext import Updater

# اطلب من المستخدم إدخال رمز البوت عند تشغيل البرنامج
TOKEN = input("الرجاء إدخال رمز بوت تلجرام الخاص بك: ")
bot = Bot(token=TOKEN)

# قم بتعيين معرف المستخدم الخاص بك هنا
user_id = "YOUR_TELEGRAM_USER_ID"

def convert_to_anime_style(update: Update, context: CallbackContext) -> None:
    if update.message.photo:
        photo = update.message.photo[-1]
        file_id = photo.file_id
        newFile = bot.get_file(file_id)
        newFile.download('input_image.jpg')
        convert_to_anime_style('input_image.jpg', 'anime_output.jpg')
        with open('anime_output.jpg', 'rb') as photo:
            bot.send_photo(update.message.chat_id, photo)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("أهلاً! قم بإرسال صورة لتحويلها إلى أنمي.")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, convert_to_anime_style))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
