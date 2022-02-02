'''Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге, читает его и выводит два слова:
наиболее часто встречающееся из тех, что имеют размер более трех символов, и наиболее длинное слово на английском языке.
В файле ожидается смешанный текст на двух языках — русском и английском.'''

import string  # модуль для работы с объектами str
# функция, которая определяет слово(а) наиболее часто встречающнееся в тексте
def count_word(text):
    count = {}  # вводим словарь {слово: количество в тексте} для подсчета вхождений слова в тексте
    for word in text:  # считаем слова, добавляем в словарь
        if len(word) > 3:  # рассматриваем слова больше 3х символов
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    max_count = (max(count.values()))  # находим максимальное количество вхождений
    # вводим словарь из слов, которые встречаются наиболее часто (таких слов может быть несколько)
    count_max = {word: count for word, count in count.items() if count == max_count}
    # выводим наиболее часто встречающееся слова
    n = 0 # счетчик
    for word, count in count_max.items():
        if n > 0:
            print(f'А также слово "{word}" (встречается в тексте  {count} раз)')
        else:
            print(f'Слово "{word}" встречается в тексте наиболее часто - {count} раз')
        n += 1
    return True

# функция, которая находит наиболее длинное слово на английском языке
def len_eng_word(text):
    word_len = {}  #словарь {слово: длина} 
    english = "abcdefghijklmnopqrstuvwxyz'"  # английский алфафит
    for word in text:
        if word[0] in english: # если слово английское
            if word not in word_len:
                word_len[word] = len(word) # добавляем в словарь слово - длина
    max_len = max(word_len.values())
    # вводим словарь из слов, с наибольшей длинной (таких слов может быть несколько)
    word_len_max = {word: lens for word, lens in word_len.items() if lens == max_len}
    n = 0 # счетчик
    for word, lens in word_len_max.items():
        if n > 0:
            print(f'А также слово - "{word}", его длина тоже {lens} символов.')
        else:
            print(f'Самое длинное английское слово в тексте - "{word}", его длина {lens} символов.')
        n += 1
    return True

file = input('Введите имя файла\n')
txt = '.txt'
if txt not in file:  # добавляем расширение файла, если пользователь его не ввел
    file += txt

try: # ловим ошибку отсутствия файла
    with open(file, encoding='utf8') as text:
        text_str = text.read()  # передадим содержимое файла в строку
        text_str = text_str.lower()  # переводим в нижний регистр
        # уберем всю понктуацию и переносы из текста(кроме) символа '  - будем считать его частью английского слова, например It's, I'm 
        text_str = text_str.replace('\n', ' ')
        string.punctuation += '—«»'  # символы пунктуации
        for p in string.punctuation:
            if not p == "'":
                text_str = text_str.replace(p, '')
        # print(text_str)
        text_list = list(text_str.split())  # перегоняем строку в список из слов
except FileNotFoundError as e:
    print(f'Файл "{file}" не найден в текущей директории.\nПроверьте имя файла или скопируйте файл в текущую папку и запустите программу заново')
else:      
    if text_list == []: # проверяем не пустой ли файл
        print(f'Файл "{file}" не содержит текста. Перезапустите программу и попробуйте открыть другой файл')
        exit() # если пустой, выходим из программы
    
    count_word(text_list)
    print('---------------')
    len_eng_word(text_list)
             
            
        

