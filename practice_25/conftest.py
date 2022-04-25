import pytest
import uuid
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Функция помогает детектить падение тестов
    # и давать об этом информацию в teardown
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def get_chrome_options(chrome_options):
    '''Фикстура настройки опций драйвера браузера Хром'''
    options = chrome_options
    options.add_argument('chrome')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options= options)
    return driver

@pytest.fixture
def web_browser(get_webdriver, request):
    driver = get_webdriver
    # Return browser instance to test case:
    yield driver # мы используем yield для продолжения функции после окончания теста
    '''Вспомним, как работает команда yield, — так же как и return, она передаёт значение
     на выход функции, но не завершает её, а «ставит на паузу». Когда кусок кода, 
     в котором вызывалась наша функция, будет завершён, мы вернёмся обратно в неё 
     и выполним оставшиеся команды.'''
    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            # uuid.uuid4() создает случайный UUID объекта
            driver.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # For happy debugging:
            print('URL: ', driver.current_url)
            print('Browser logs:')
            for log in driver.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here
    driver.quit()


@pytest.fixture
def testing(get_webdriver):
   pytest.driver = get_webdriver
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()