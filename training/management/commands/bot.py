import os
import gym_app.wsgi
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
from django_currentuser.middleware import get_current_user


os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from training.models import Workout, Profile

TOKEN = '1181578693:AAHvArBcv1w621lI-dMPEDAzyJFFyMXrsXQ'

PROXY_URL = 'https://telegg.ru/orig/bot'

button_help = 'Помощь'

# tasks = Workout.objects.all()
# for task in tasks:
#     u = "Evgeniy"
#     if str(task.user) == u:
#         print(task.start_time)

#print(tasks)

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
    date_lst = []
    text = update.message.text
    tasks = Workout.objects.all()
    for task in tasks:
        if text == str(task.user):
            date_lst.append(task.start_time)
    reply_text = "Your next workout at {}".format(date_lst[-1])
    update.message.reply_text(
        text=reply_text
    )


def main():
    print('Start')

    req = Request(
        connect_timeout=0.5,
    )
    bot = Bot(
        request=req,
        token=TOKEN,
        base_url=PROXY_URL,
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
