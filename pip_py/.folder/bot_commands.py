from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import emoji

def hello_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello, {update.effective_user.first_name}!')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hello - приветствие пользователя\n/time - время\n/help - справка\n'\
        '/sum - выводит сумму двух чисел, введённых через пробел\n/dif - выводит разность двух чисел\n'\
        '/love - бот любит тебя')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

def dif_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x-y}')

def love_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(emoji.emojize(f'Я люблю тебя! Не грусти :red_heart:'))