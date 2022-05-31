from telebot import types # для создания кнопок
# прикручиваем клавиатуру

#Клавиатура главного меню
markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, количество кнопок по одной в ряду
itembtn1 = types.KeyboardButton('Конвертер') #Название кнопки 1
itembtn2 = types.KeyboardButton('Доступные валюты') #Название кнопки 2
itembtn3 = types.KeyboardButton('Помощь') #Название кнопки 3
itembtn4 = types.KeyboardButton('Основные команды') #Название кнопки 4
markup.add(itembtn1, itembtn2, itembtn3, itembtn4) #Занесение кнопок в матрицу
#Клавиатура главного меню

#Клавиатура  меню Конвертер
markup_val = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Активация, название, количество кнопок по одной в ряду
itembtn1_1 = types.KeyboardButton('Евро') #Название кнопки 1
itembtn1_2 = types.KeyboardButton('Доллар') #Название кнопки 2
itembtn1_3 = types.KeyboardButton('Рубль') #Название кнопки 3
itembtn1_4 = types.KeyboardButton('Биткоин') #Название кнопки 4
itembtn1_5 = types.KeyboardButton('Основное меню') #Название кнопки 5
markup_val.add(itembtn1_1, itembtn1_2, itembtn1_3, itembtn1_4, itembtn1_5) #Занесение кнопок в матрицу
#Клавиатура  меню Конвертер


