# прикепляем бота
from extensions import ConverterBot, ConvertationException
from config import TOKEN, money, s, text_start, text_help
from menu import markup, markup_val
import telebot
# создаем объект Telebot
bot = telebot.TeleBot(TOKEN)
base, quote, amount = '', '', ''
# обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, text_start, reply_markup=markup) # бот отправляет сообщение (send_message) в чат (message.chat.id)
# обработчик команды /start

# обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, text_help, reply_markup=markup)
# обработчик команды /help

# обработчик команды /values
@bot.message_handler(commands=['values', ])
def handle_start_help(message):
    text = f'Доступные валюты:\n{s}\n/help - помощь.'
    bot.send_message(message.chat.id, text, reply_markup=markup) # бот отправляет сообщение (send_message) в чат (message.chat.id)
# обработчик команд /values

## обработчик текстовых сообщений
@bot.message_handler(content_types = ['text', ])
def handle_convert(message: telebot.types.Message):
    try: # ловим ошибку сервера
        global base, quote, amount
        text_split = message.text.split() # разбиваем текст
        if len(text_split) == 3: # ручной ввод
            base, quote, amount = text_split
            total = ConverterBot.get_price(base.title(), quote.title(), amount)
            text = f'Цена {amount} {base.lower()} в {quote.lower()} составляет {total}'
            bot.send_message(message.chat.id, text)
            base, quote, amount = '', '', '' # обнуляем значения, для нового расчета
    # дополнительный функционал (управление кнопками)
        if message.text == 'Основное меню':
            base, quote, amount = '', '', ''  # обнуляем значения, для нового расчета
            bot.send_message(message.chat.id, 'Приступим?)', reply_markup=markup)
        elif quote: # если вторая валюта выбрана, конвертируем
            try:
                amount = float(message.text)
            except ValueError:
                raise ConvertationException(f'Не удалось обработать количество "{message.text}"')
            total = ConverterBot.get_price(base.title(), quote.title(), amount)
            text = f'Цена {amount} {base.lower()} в {quote.lower()} составляет {total}'
            base, quote, amount = '', '', '' # обнуляем значения, для нового расчета
            bot.send_message(message.chat.id, text)
        elif message.text in money.keys(): # если евро, или доллар, или рубль, или биткоин
            if not base: # если еще не выбрана первая валюта
                base = message.text
                bot.send_message(message.chat.id, 'Выбери во что будем конвертировать', reply_markup=markup_val)
            else:
                if not quote: # если еще не выбрана вторая валюта
                    quote = message.text
                    bot.send_message(message.chat.id, 'Введи количество', reply_markup=markup_val)
    # нажатие на кнопки
        elif message.text == 'Помощь':
            bot.send_message(message.chat.id, text_start, reply_markup=markup)
        elif message.text == 'Доступные валюты':
            bot.send_message(message.chat.id, f'Доступные валюты:\n{s}\n/help - помощь.', reply_markup=markup)
        elif message.text == 'Конвертер':
            bot.send_message(message.chat.id, 'Выбери что будем конвертировать', reply_markup=markup_val)

        elif message.text == 'Основные команды':
            bot.send_message(message.chat.id, '/start    - давай знакомиться\n/help     - помощь\
            \n/values - список доступных валют', reply_markup=markup)
        elif len(text_split) != 3: # неверный ввод
            raise ConvertationException()
        '''else:
            if  message.text == 'Основное меню': # возвращаемся в основное меню из ошибки
                base, quote, amount = '', '', ''  # обнуляем значения, для нового расчета
                bot.send_message(message.chat.id, 'Приступим?)', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Давай попробуем заново))', reply_markup=markup)'''
    except ConvertationException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}\nПовторите ввод или вернитесь в Основное меню:', reply_markup=markup_val)
    except Exception as e:
        bot.reply_to(message, f'Ошибка сервера. Не удалось обработать команду\n{e}')


# запускаем бота
bot.polling(none_stop=True) 