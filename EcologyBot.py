import os
import telebot
import requests
import random

bot = telebot.TeleBot("8565732472:AAEJo8ytHivnZFkDR-Daqeqe8bbfexeaoOU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот, созданный для сохранения природы. Чтобы узнать, что я умею, напиши /info")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "/clean_use, /bottles, /posters")


@bot.message_handler(commands=['clean_use'])
def send_clean(message):
    bot.reply_to(message, 'Чтобы сохранить природу, нужно сокращать потребление пластика (который разлагается около 400 лет), воды, энергии, правильно утилизировать отходы (сортировать мусор, сдавать батарейки(которые приносят вред окружающей среде))')

@bot.message_handler(commands=['bottles'])
def send_clean(message):
    bot.reply_to(message, 'Из пластиковых бутылок можно делать кормушки для птиц.')
    bot.send_photo(message.chat.id, photo='https://lh5.googleusercontent.com/proxy/rQzFqsiJy4yEkS8dRR8NMBOzoa4CvirdJQwNRITqqJDfDB9wXRCyqDi3ffrhgrAcCyPm53mmuV2PCkwqydMpGJDOoha1NWFiS8mNtZbcPOikIIOgjyGWrEXjcji5CK6Cthr2occP')

@bot.message_handler(commands=['posters'])
def posters(message):
    url = random.choice(['https://www.osinniki.org/uploads/posts/2022-10/ekbupzmxphm.webp', 'https://nevyansk66.ru/media/project_mo_101/1c/64/09/65/62/6c/beregite_prirodu_1_12151221.jpg', 'https://neya.smi44.ru/wp-content/uploads/2023/04/%D0%B1%D1%83%D0%B4%D1%8C%D1%82%D0%B5-%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D1%8B-%D0%BA-%D0%BF%D1%80%D0%B8%D1%80%D0%BE%D0%B4%D0%B5-%D0%BD%D0%B5-%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F-752x440.jpg'])
    bot.send_photo(message.chat.id, url)

bot.polling()