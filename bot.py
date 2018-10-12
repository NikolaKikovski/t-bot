import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='559070915:AAFy9gak-JOQwvhQj7xsFw0VA1jpIt3a1Lo') # Токен API к Telegram
dispatcher = updater.dispatcher

def get_answer():
    response = requests.get('https://yesno.wtf/api')
    return response.json()


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Send me a question')
def textMessage(bot, update):
    response = get_answer()
    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()