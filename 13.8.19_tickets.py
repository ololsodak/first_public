'''Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:

1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.

2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:

        Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
        От 18 до 25 лет — 990 руб.
        От 25 лет — полная стоимость 1390 руб.

3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на конференцию,
 то дополнительно получает 10% скидку на полную стоимость заказа.'''
tickets = int(input('Введите необходимое количество билетов на онлайн-конференцию:\n')) # количество билетов
price = 0 # вводим переменную для подсчета общей суммы
for i in range(1,tickets+1):
    years = int(input(f'Введите возраст {i}-го посетителя:\n')) # возраст посетителя
    if 18 <= years < 25:
        price += 990
    elif years >= 25:
        price += 1390
# Выводим общую сумму        
if price == 0:
    print(f'Ваши билеты бесплатны, так как возраст посетителей менее 18 лет')
else:
    if tickets > 3:
        price -= 0.1*price
        print(f'Общая сумма для оплаты ваших {tickets} билетов (с учетом скидки 10%) - {round(price)} руб.')
    else:
        print(f'Общая сумма для оплаты ваших {tickets} билетов - {round(price)} руб.')
    