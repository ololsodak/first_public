#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time
import pytest
from pages.akusherstvo import AkusherstvoRu


@pytest.mark.parametrize('item', ['коляска', 'молоко', 'кукла', 'сок'])
@pytest.mark.parametrize('n', [3, 2, 4])
def test_check_count_in_basket(web_browser, item, n):
    """Make sure that calculator in the cart works well. """
    page = AkusherstvoRu(web_browser)
    # Ищем товар
    page.search.send_keys(item)
    page.search_btn.click()
    # Нажимаем кнопку сортировки по возрастанию цены
    page.sort_btn.click()
    page.sort_by_price_up.click()
    # Добавляем n-ый товар в корзину
    page.buy_btns[n].click()
    page.cart.click()
    # Увеличиваем количество товара
    for i in range(n-1):
        page.cart_plus_btn.click()
        time.sleep(1)
    # Получаем цену единицы товара
    price_item = page.cart_price_one.get_text()
    price_item = price_item.split(' ')
    # Итоговая цена товара
    result_price = page.cart_price.get_text()
    # Конвертируем в число
    result_price = float(result_price.replace(' ', ''))
    print('\nЦена единицы товара - ', float(price_item[0]))
    print(f'Итоговая цена - {n}*{float(price_item[0])} = ', result_price)
    # проверка калькулятора итоговой цены товара в корзине
    assert n*float(price_item[0]) == result_price
    # Очистка корзины
    page.cart_list.move_to_element()
    page.cart_del_icon.click()
