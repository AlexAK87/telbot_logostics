import telebot;
from telebot import types



bot = telebot.TeleBot('5186827794:AAHGfysPZ6fMakSInFccOdRfMprY-2z1iIU');


@bot.message_handler(content_types=['text'])
def start(message):
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    reply_markup = types.ReplyKeyboardMarkup();
    resize_keyboard = reply_markup.resize_keyboard;

    if message.text == '/reg':
        bot.send_message(message.from_user.id, 'Выберите раздел в меню', reply_markup='{"name":"John", "age":30, "city":"New York"}')
        #{
        #reply_markup: {
        #    resize_keyboard: True,
        #    keyboard: [
        #        ['Мои задачи'],
        #        ['Работа с клиентом'],
        #        ['Номенклатура и остатки'],
        #        ['Автопарк'],
        #        ['Поставить задачу'],
        #        ['Кадры и справки'],
        #        ['На главную'],
        #        ['Выйти из приложения']
        #      ]
        #   }
        #});
        
        #bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

bot.polling(none_stop=True, interval=0) 