import os
import gym_app.wsgi
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.utils.request import Request
from training.models import Workout

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

TOKEN = '1181578693:AAHvArBcv1w621lI-dMPEDAzyJFFyMXrsXQ'

PROXY_URL = 'https://telegg.ru/orig/bot'


def log_error(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e

    return inner


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
        text=reply_text[:-9]
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
