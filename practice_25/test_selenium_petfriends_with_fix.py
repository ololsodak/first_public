from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from setings import my_email, my_password

@pytest.mark.usefixtures('testing')
def test_show_all_pets(email = my_email, password = my_password):
    '''Тест проверки карточек питомцев на странице Все притомцы'''
    # задаем неявное ожидание элементов
    pytest.driver.implicitly_wait(5)
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys(email)
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys(password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    # Далее применим множественный поиск элементов на странице
    # Поиск фото питомцев
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    # поиск имени
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    # поиск описания (тип, возраст)
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
    print('----', names)
    for i in range(len(names)):
        # для картинки смотрим атрибут "src"
        assert images[i].get_attribute('src') != ''
        # для имени, что есть тест
        assert names[i].text != ''
        # для типа и возраста
        # что текст не пустой
        assert descriptions[i].text != ''
        # что есть запятая-разделитель (Чтобы убедиться, что в данном элементе выводится и возраст, и тип питомца)
        assert ', ' in descriptions[i]
        # Чтобы убедиться, что в строке есть и возраст питомца, и его вид, мы разделяем строку по запятой
        # и ждём, что каждая из частей разделённой строки будет длиной больше нуля
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

@pytest.mark.usefixtures('testing')
def test_show_my_pets(email = my_email, password = my_password):
    '''Тест, который проверяет, что на странице со списком питомцев пользователя:
        1. Присутствуют все питомцы.
        2. Хотя бы у половины питомцев есть фото.
        3. У всех питомцев есть имя, возраст и порода.
        4. У всех питомцев разные имена.
        5. В списке нет повторяющихся питомцев. (Сложное задание).
    '''
    pytest.driver.find_element_by_id('email').send_keys(email)
    pytest.driver.find_element_by_id('pass').send_keys(password)
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # задаем ожидание кнопки "Мои питомцы" на главной странице
    wait = WebDriverWait(pytest.driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/my_pets"]')))
    # Кликаем по кнопке 'Мои поитомцы'
    pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
    # задаем ожидание элемента "Статистика" на странице пользователя
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))
    # определяем количество строк в таблице питомцев пользователя
    strings = pytest.driver.find_elements_by_xpath('//tbody/tr')
    # Определяем количество питомцев элемента статистики пользователя
    statistic = pytest.driver.find_elements_by_css_selector('.\\.col-sm-4.left')
    number_pets = statistic[0].text.split('\n')
    number_pets = number_pets[1].split(' ')
    number_pets = int(number_pets[1])
    print('\n',number_pets, len(strings))
    # Тест 1. Присутствуют все питомцы.
    assert number_pets == len(strings)
    # Поиск фото питомцев
    images = pytest.driver.find_elements_by_xpath('//th[@scope="row"]/img')
    # Поиск имен питомцев
    names = pytest.driver.find_elements_by_xpath('//tr/td[1]')
    # Поиск пород питомцев
    animal_types = pytest.driver.find_elements_by_xpath('//tr/td[2]')
    # Поиск возрастов питомцев
    ages = pytest.driver.find_elements_by_xpath('//tr/td[3]')
    n = 0 #  счетчик питомцев с  фото
    for i in range(len(strings)):
        if images[i].get_attribute('src') != '':
            n += 1
        # Тест 3. У всех питомцев есть имя, возраст и порода
        assert names[i].text != '' # имя
        assert  animal_types[i].text != '' # порода
        assert ages[i].text != '' # возраст
        # проверяем, что у всех питомцев разные имена
        # (повторяющиеся питомцы — это питомцы, у которых одинаковое имя, порода и возраст).
        for j in range(i+1, len(strings)):
            # Тест 4. У всех питомцев разные имена.
            assert names[i].text != names[j].text
            # Тест 5. В списке нет повторяющихся питомцев
            if names[i].text == names[j].text:
                if animal_types[i].text == animal_types[j].text:
                    assert ages[i].text != ages[j].text
    # Тест 2. Хотя бы у половины питомцев есть фото
    assert n >= len(strings) / 2