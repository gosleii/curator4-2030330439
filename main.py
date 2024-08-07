import telebot
bot=telebot.TeleBot('7162879905:AAELLaklld4llJtbDPbYIilEQ96dSMtiWx0')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'[Добро пожаловать в мой телеграмм канал:](https://t.me/+gyEFyuWKK39jNzI6)', parse_mode='Markdown')

@bot.message_handler(commands=['school'])
def main(message):
    bot.send_message(message.chat.id,'[Хей, лови ссылку на тг лучшей профильной школы Красноярска:](https://t.me/fms_sfu)', parse_mode='Markdown')

@bot.message_handler(commands=['news'])
def main(message):
    bot.send_message(message.chat.id,'[Все новости Красноярска только тут:](https://t.me/krasnoyaarsk)', parse_mode='Markdown')

@bot.message_handler(commands=['names'])
def m(message):
    bot.send_message(message.chat.id,'Введите имя бота, но учтите, что оно должно быть менее 20 символов, начинается не с цифры и заканчивается на слово bot', parse_mode='Markdown')

def a(message):
    if len(message)<=20 and message[0] not in '1234567890' and (message[-3]=='b' and message[-2]=='o' and message[-1]=='t'):
        bot.send_message(message.chat.id,'Ник одобрен!', parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, 'В нике допущена ошибка!', parse_mode='Markdown')

bot.infinity_polling()