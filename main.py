import os
import telebot

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Bot de Links Activo! Mandame algo para probar.")

bot.infinity_polling()
