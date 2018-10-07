from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
PROXY = {'proxy_url' : 'socks5://t1.learn.python.ru:1080','urllib3_proxy_kwargs': {'username': 'learn','password': 'python'}}

def start_bot(bot, update):
    mytext = "Привет {}! Я простой бот и понимаю только команду {}". format(update.message.chat.first_name, '/start')

    update.message.reply_text(mytext)



def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)


def main():
    updtr = Updater((settings.TELEGRAM_API_KEY),request_kwargs=PROXY)
    dp = updtr.dispatcher
    dp.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    main()