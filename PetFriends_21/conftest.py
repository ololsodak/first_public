import os, pytest, json, requests, datetime
from settings import my_email, my_password, my_email2, my_password2, not_valid_password, not_valid_mail, base_url

@pytest.fixture(autouse=True)
def request_fixture(request):
    print(f"\nЗапущен тест: {request.function.__name__}")


@pytest.fixture(scope='class',autouse=True)
def get_key():
    '''метод запроса ключа'''
    # данные передаются в заголовке
    headers = {
        'email': my_email2,
        'password': my_password2
        }
    # отправляем запрос
    res = requests.get(base_url + 'api/key', headers=headers)
    status = res.status_code
    assert status == 200
    try:
        auth_key = res.json()
    except json.decoder.JSONDecodeError as e:
        auth_key = res.text
    print(auth_key)
    return auth_key

@pytest.fixture()
def invalid_key():
    '''метод запроса ключа'''
    # данные передаются в заголовке
    headers = {
        'email': not_valid_mail,
        'password': not_valid_password
        }
    # отправляем запрос
    res = requests.get(base_url + 'api/key', headers=headers)
    status = res.status_code
    assert status == 403
    try:
        auth_key = res.json()
    except json.decoder.JSONDecodeError as e:
        auth_key = res.text
    print(auth_key)
    return auth_key

@pytest.fixture(autouse=True) # чтобы не прописывать фикстуру в параметрах теста каждый раз
def time_delta():
    start_time = datetime.datetime.now()
    yield
    finish_time = datetime.datetime.now()
    print(f'\nВремя выполнения теста - {finish_time-start_time}\n---------')
#pf = PetFriendsFixture()
#print(get_api_key())