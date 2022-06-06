import os
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AkusherstvoRu(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.akusherstvo.ru/'
        super().__init__(web_driver, url)

    search = WebElement(id='search_data')  # Поле поиска
    search_btn = WebElement(class_name='search__btn')  # Кнопка поиска
    cart = WebElement(class_name='cart__title')  # Корзина
    # Строка ввода количества товаров в корзине
    cart_input = WebElement(css_selector='.js-qty-input.counter-cart__input')
    # Названия товаров в корзине
    cart_list = WebElement(class_name='cart-list__title-name')
    cart_del_icon = WebElement(css_selector='.close.js-btn-close')  # Иконка Удалить из корзины
    # Кнопка увеличения количества товара
    cart_plus_btn = WebElement(css_selector='.counter-cart__btn.counter-cart__btn--minus.js-btn-plus  ')
    # Цена за единицу товара в корзине
    cart_price_one = WebElement(css_selector='.cart-list__price_small.js-price-normal ')
    # Итоговая цена товара в корзине
    cart_price = WebElement(css_selector='.cart-list__sum-value.js-price-sum')
    # Названия товаров в поиске
    products_titles = ManyWebElements(xpath='//p/a[contains(@href, "/catalog/") and @data-tid!=""]')
    # Цены товаров
    products_prices = ManyWebElements(css_selector='.valuePrice.js-price-normal')
    buy_btns = ManyWebElements(css_selector='.btn.btn--primary.btn--small.btn--catalogpage')  # Кнопки купить
    # Кнопка сортировки выпадающая
    sort_btn = WebElement(class_name='small-nav__close')
    # Кнопка сортировки по возрастанию цены
    sort_by_price_up = WebElement(xpath='//span[text()="цене ↑"]')
    # Кнопка сортировки по убыванию цены
    sort_by_price_down = WebElement(xpath='//span[text()="цене ↓"]')
    # Кнопка подменю Детская мебель
    submenu_furniture = WebElement(xpath='//a[@href="/detskaya-mebel/"]')
    # Кнопка подменю Коляски
    submenu_strollers = WebElement(xpath='//a[@href="/detskie-kolyaski/"]')
    # Кнопка подменю Автокресла
    submenu_car_seats = WebElement(xpath='//a[@href="/detskie-avtokresla/"]')
    # Кнопка подменю Транспорт
    submenu_transport = WebElement(xpath='//a[@href="/detskij-transport/"]')
    # Кнопка подменю Детская одежда
    submenu_clothes = WebElement(xpath='//a[@href="/detskaya-odezhda/"]')
