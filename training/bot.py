from telegram import Bot
from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.utils.request import Request

from datetime import date



button_help = 'Помощь'

req = Request(
        connect_timeout=0.5,
    )
bot = Bot(
        request=req,
        token='1181578693:AAHvArBcv1w621lI-dMPEDAzyJFFyMXrsXQ',
        base_url='https://telegg.ru/orig/bot',
    )
updater = Updater(
        bot=bot,
        use_context=True,
    )

recycling_days = ['2020-10-29', '2020-10-31']

today = date.today()


def log_error(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e

    return inner


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Это помощь!',
        reply_markup=ReplyKeyboardRemove(),
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    # if text == button_help:
    #     return button_help_handler(update=update, context=context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='othser'),
            ],
        ],
        resize_keyboard=True,
    )

    if str(today) in recycling_days:
        update.message.reply_text(
            text='Привет ты записан!',
            reply_markup=reply_markup,
    )


def main():
    print('Start')

    req = Request(
        connect_timeout=0.5,
    )
    bot = Bot(
        request=req,
        token='1181578693:AAHvArBcv1w621lI-dMPEDAzyJFFyMXrsXQ',
        base_url='https://telegg.ru/orig/bot',
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

    print('Finish')


if __name__ == '__main__':
    main()
