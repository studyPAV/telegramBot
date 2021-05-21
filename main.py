import logging
from  telegram.ext import Updater, CommandHandler, CallbackContext
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='easyBot.log'
                    )
def starBot( update: Updater, context: CallbackContext):
    MsgStart="Hello {}, I have only \start command".format(update.message.chat.first_name)
    update.message.reply_text(MsgStart)
    print(update)
def main():
    logging.info('Bot started')
    updt = Updater('1543790474:AAFh4fHxVBv9RpS90KhM8wQiuzZbFHi2ZXw')
    updt.dispatcher.add_handler(CommandHandler("start", starBot))
    updt.start_polling()
    updt.idle()



if __name__== "__main__":
    main()

