import cv2
from deepart import deepart
from telegram import Bot
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters
from telegram.ext import Updater

# قم بتعيين رمز بوت تلجرام الخاص بك هنا
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=TOKEN)

# قم بتعيين معرف المستخدم الخاص بك هنا
user_id = "YOUR_TELEGRAM_USER_ID"

def convert_to_anime_style(update: Update, context: CallbackContext) -> None:
    # قم بالتحقق مما إذا كانت الرسالة تحتوي على صورة
    if update.message.photo:
        # حدد أكبر صورة مرسلة
        photo = update.message.photo[-1]
        # قم بتنزيل الصورة
        file_id = photo.file_id
        newFile = bot.get_file(file_id)
        newFile.download('input_image.jpg')

        # تحويل الصورة إلى أنمي
        convert_to_anime_style('input_image.jpg', 'anime_output.jpg')

        # إرسال الصورة المحولة
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
