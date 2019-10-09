from telegram.ext import Updater, CommandHandler
from key import KEY

TOKEN = KEY

def hello(bot, update):
    update.message.reply_text(
        'Contribute for Hacktoberfest, {}!'.format(update.message.from_user.first_name))

def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CommandHandler('hacktoberfest', hello))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
