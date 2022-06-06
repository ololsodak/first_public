#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
from pages.akusherstvo import AkusherstvoRu


@pytest.mark.parametrize('item', ['подгузники', 'сок', 'коляска', 'мяч', 'смесь', 'самокат', 'ролики'])
def test_check_basket(web_browser, item):
    """Make sure that adding an item to the cart works well. """
    page = AkusherstvoRu(web_browser)
    page.search.send_keys(item)
    page.search_btn.click()
    page.buy_btns[0].click()
    page.cart.click()
    assert page.get_current_url() == 'https://www.akusherstvo.ru/magaz.php?action=show_basket'
    msg = 'Wrong product in cart'
    assert item in page.cart_list.get_text().lower(), msg
    # Очистка корзины
    page.cart_list.move_to_element()
    page.cart_del_icon.click()


@pytest.mark.parametrize("item", [('gjluepybrb', 'подгузники'),
                                  ('cjr', 'сок'),
                                  ('rjkzcrf', 'коляска'),
                                  ('vzx', 'мяч'),
                                  ('gjleirf', 'подушка'),
                                  ('rhtckj', 'кресло'),
                                  ('gkfcnbkby', 'пластилин')])
def test_check_wrong_input_in_search(web_browser, item):
    """Make sure that wrong keyboard layout input works fine. """
    (inputs, expected_output) = item
    page = AkusherstvoRu(web_browser)
    page.search.send_keys(inputs)
    page.search_btn.click()
    # Verify that user can see the list of products:
    assert page.products_titles.count() == 52
    # Make sure user found the relevant products
    print(page.products_titles.get_text())
    for title in page.products_titles.get_text():
        if title:
            msg = 'Wrong product in search "{}"'.format(title)
            assert expected_output in title.lower(), msg


@pytest.mark.parametrize("item", ['подгузники', 'пластилин', 'мяч', 'кресло', 'автокресло', 'самокат', 'пенка'])
def test_check_input_in_search(web_browser, item):
    """Make sure main search works fine. """
    page = AkusherstvoRu(web_browser)
    page.search.send_keys(item)
    page.search_btn.click()
    # Verify that user can see the list of products
    assert page.products_titles.count() == 52
    # Make sure user found the relevant products
    print(page.products_titles.get_text())
    for title in page.products_titles.get_text():
        if title:
            msg = 'Wrong product in search "{}"'.format(title)
            assert item in title.lower(), msg


@pytest.mark.parametrize("item", ['автокресло', 'пластилин', 'мяч', 'кресло', 'подгузники', 'самокат', 'пенка'])
def test_check_sort_by_price_up(web_browser, item):
    """Make sure that sort by price up works fine.  """
    page = AkusherstvoRu(web_browser)
    page.search.send_keys(item)
    page.search_btn.click()
    # Нажимаем кнопку сортировки по возрастанию цены
    page.sort_btn.click()
    page.sort_by_price_up.click()
    page.wait_page_loaded()
    # Получаем словарь цен товаров
    all_prices = page.products_prices.get_text()
    # Конвертируем в число
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print(all_prices)
    print(sorted(all_prices))
    # Проверяем, что сортировка работает
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"


@pytest.mark.parametrize("item", ['автокресло', 'пластилин', 'мяч', 'кресло', 'подгузники', 'самокат', 'пенка'])
def test_check_sort_by_price_down(web_browser, item):
    """Make sure that sort by price down works fine."""
    page = AkusherstvoRu(web_browser)
    page.search.send_keys(item)
    page.search_btn.click()
    # Нажимаем кнопку сортировки по убыванию цены
    page.sort_btn.click()
    page.sort_by_price_down.click()
    page.wait_page_loaded()
    # Получаем словарь цен товаров
    all_prices = page.products_prices.get_text()
    # Конвертируем в число
    all_prices = [float(p.replace(' ', '')) for p in all_prices]
    print('\n', all_prices)
    print(sorted(all_prices, reverse=True))
    # Проверяем, что сортировка работает
    assert all_prices == sorted(all_prices, reverse=True), "Sort by price doesn't work!"
