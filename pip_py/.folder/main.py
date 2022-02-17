from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5165531969:AAEeB3__9z-JtH6_lrI7zVPs-NJGNlHvBqQ')

updater.dispatcher.add_handler(CommandHandler('hello', hello_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('dif', dif_command))
updater.dispatcher.add_handler(CommandHandler('love', love_command))

print('server start')
updater.start_polling()
updater.idle()