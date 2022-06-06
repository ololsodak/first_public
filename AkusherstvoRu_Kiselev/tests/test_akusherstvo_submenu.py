#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time
from pages.akusherstvo import AkusherstvoRu


def test_submenu_furniture(web_browser):
    """Make sure that submenu furniture works fine."""
    page = AkusherstvoRu(web_browser)
    page.submenu_furniture.click()
    page.scroll_down()
    time.sleep(3)
    page.scroll_up()
    assert page.get_current_url() == 'https://www.akusherstvo.ru/detskaya-mebel/'


def test_submenu_strollers(web_browser):
    """Make sure that submenu strollers works fine."""
    page = AkusherstvoRu(web_browser)
    page.submenu_strollers.click()
    page.scroll_down()
    time.sleep(3)
    page.scroll_up()
    assert page.get_current_url() == 'https://www.akusherstvo.ru/detskie-kolyaski/'


def test_submenu_car_seats(web_browser):
    """Make sure that submenu car seats works fine."""
    page = AkusherstvoRu(web_browser)
    page.submenu_car_seats.click()
    page.scroll_down()
    time.sleep(3)
    page.scroll_up()
    assert page.get_current_url() == 'https://www.akusherstvo.ru/detskie-avtokresla/'


def test_submenu_transport(web_browser):
    """Make sure that submenu transport works fine."""
    page = AkusherstvoRu(web_browser)
    page.submenu_transport.click()
    page.scroll_down()
    time.sleep(3)
    page.scroll_up()
    assert page.get_current_url() == 'https://www.akusherstvo.ru/detskij-transport/'


def test_submenu_clothes(web_browser):
    """Make sure that submenu clothes works fine."""
    page = AkusherstvoRu(web_browser)
    page.submenu_clothes.click()
    page.scroll_down()
    time.sleep(3)
    page.scroll_up()
    assert page.get_current_url() == 'https://www.akusherstvo.ru/detskaya-odezhda/'
