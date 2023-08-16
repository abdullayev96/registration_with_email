from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import CommandHandler,Updater

from web import settings

from telegram.utils.request import Request


def start_handler(update, context):
    update.message.reply_text("Assalamu alaykum hush kelibsz ")


class Command(BaseCommand):
    help = 'Telegram bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )

        bot = Bot(
            request=request,
            token=settings.TOKEN,
            # base_url=settings.PROXY_URL,
        )

        updater = Updater(bot=bot,use_context=True,)


        updater.dispatcher.add_handler(CommandHandler('start', start_handler))
        # updater.dispatcher.add_handler(MessageHandler(Filters.text, handler))
        # updater.dispatcher.add_handler(CallbackQueryHandler(search))
        # updater.dispatcher.add_handler(CallbackQueryHandler(callback_tasks))

        updater.start_polling()
        updater.idle()
