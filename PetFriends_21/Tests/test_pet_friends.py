import os
import pytest

from api import PetFriends
from settings import my_email, my_password, my_email2, my_password2, not_valid_password, not_valid_mail
# вводим объект класс PetFriends
pf1 = PetFriends()
#pf = PetFriendsFixture()
class TestPet:
    @pytest.mark.get
    def test_get_api_key_for_valid_user(self, get_key):
        ''' Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key'''

       # assert status == 200
        assert 'key' in get_key

    @pytest.mark.get
    def test_get_all_pets_for_valid_user(self, get_key, filter = ''): # передаем только фильтр
        ''' Проверяем что запрос всех питомцев возвращает не пустой список.'''
        status, result = pf1.get_list_of_pets(get_key, filter)
        assert status == 200
        assert len(result['pets']) > 0

    @pytest.mark.post
    def test_add_new_pet_with_photo_successfully(self, get_key, name= 'Жаба Петровна', animal_type='Лама', age='3', pet_photo='images/lama.jpg'):
        '''Проверяем что можно добавить питомца с корректными данными'''
        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        status, result = pf1.post_new_pet_with_photo(get_key, name,animal_type,age,pet_photo)
        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        print(result)

    @pytest.mark.delete
    def test_delete_pet_successfully(self, get_key):
        """Проверяем возможность удаления питомца"""
        # получаем данные о питомцах пользователя
        _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        # а если нет питомцев?
        if len(my_pets['pets']) == 0:
            #добавляем питомца, чтобы можно было его удалить
            pf1.post_new_pet_with_photo(get_key,'Даша','Лама','4','images/lama.jpg')
            _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        # берем id первого питомца и пробуем его удалить
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf1.delete_pet(get_key, pet_id)
        # еще раз запрашиваем список животных
        _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        # провереям, что нашего нет в списке
        assert status == 200
        assert pet_id not in my_pets.values()

    @pytest.mark.put
    def test_update_info_of_pet_successfully(self, get_key, name='Вася', anymal_type = 'крокодил', age = '1'):
        """Проверяем возможность изменения данных питомца"""
        # получаем данные о питомцах пользователя
        _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        # если список не пустой пробуем обновить данные
        if len(my_pets['pets'])>0:
            status, result = pf1.put_info_of_pet(get_key,my_pets['pets'][0]['id'],name,anymal_type,age)
            # проверяем
            assert status == 200
            assert result['name'] == name
            assert result['age'] == age
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    # Задание 19.7.2. -  10 дополнительных тестов
    # 1
    @pytest.mark.post
    def test_add_new_pet_without_photo_successfully(self, get_key,name = 'Вазген',animal_type = 'котик', age = '32'):
        '''Проверяем возможность добавления данных  о новом питомце (без фото)'''
        # запрос на сервер, добавляем нового животного
        status, result = pf1.post_new_pet_without_photo(get_key,name,animal_type,age)
        # проверяем условия
        assert status == 200
        assert result['animal_type'] == animal_type
        assert result['age'] == age

    #2
    @pytest.mark.post
    def test_add_photo_to_pet_successfully(self, get_key, pet_photo = 'images/zebra.jpg'):
        '''Проверяем возможность добавления фото для существующего питомца'''
        # получаем полный путь к фото
        pet_photo = os.path.join(os.path.dirname(__file__) , pet_photo)
        # получаем список питомцев пользователя
        _, my_pets = pf1.get_list_of_pets(get_key,'my_pets')
        # проверяем, что список не пустой, если пустой, то добавляем питомца
        if  len(my_pets['pets']) == 0:
            pf1.post_new_pet_without_photo(get_key, 'Леша', 'зебра', '5')
            _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        status, _ = pf1.set_photo_to_pet(get_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200

    #3
    @pytest.mark.get
    def test_get_my_pets_for_valid_user(self, get_key, filter = 'my_pets'):
        '''Проверяем возможность получения списка животных пользователя по фильтру my_pets'''
        status, result = pf1.get_list_of_pets(get_key, filter)
        assert status == 200
        assert len(result['pets']) > 0


    #4
    @pytest.mark.get
    def test_get_all_pets_for_not_valid_user(self, invalid_key, filter = ''):
        ''' Проверяем что запрос всех питомцев возвращает статус 403 в результате ввода не валидных данных пользователя
        Данные необходимо изменить в фикстуре get_key'''
        # status, auth_key = pf1.get_api_key(not_valid_mail, not_valid_password)
        assert "This user wasn't found in database" in invalid_key

    #5
    @pytest.mark.post
    def test_add_foto_not_corect_pet_id(self, get_key, pet_photo='images/lama.jpg'):
        """проверяем возможность добавления фото к несуществующиму питолмцу(ошибка 500)"""
        pet_id = "1234555affk444"
        status, result = pf1.set_photo_to_pet(get_key, pet_id, pet_photo)
        assert status == 500

    #6
    @pytest.mark.put
    def test_update_info_not_correct_pet_id(self, get_key,name='Вася', anymal_type = 'крокодил', age = '1'):
        """прверяем возможность изменения данных несуществующего питолмцуа(ошибка 400)"""
        # получаем данные о питомцах пользователя
        _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        # если список не пустой пробуем обновить данные
        if len(my_pets['pets'])>0:
            pet_id = "1234555affk444"
            status, result = pf1.put_info_of_pet(get_key,pet_id,name,anymal_type,age)
            # проверяем
            assert status == 400
            assert "Pet with this id wasn't found!" in result
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    #7
    @pytest.mark.get
    def test_get_pets_for_not_valid_filter(self, get_key, filter = 'me_pet'):
        '''Проверяем ошибку получения списка животных пользователя по несуществующему фильтру'''
        status, result = pf1.get_list_of_pets(get_key, filter)
        assert status == 500


    #8
    @pytest.mark.delete
    @pytest.mark.skip
    def test_delete_not_valid_pet_id(self, get_key):
        """Проверяем возможность удаления несуществующего питомца
        !!!Обнаружен баг! Сервер возвращает код 200 при попытке удаления питомца с несуществующем id!!!"""
        # получаем данные о питомцах пользователя
        _, my_pets = pf1.get_list_of_pets(get_key, 'my_pets')
        pet_id = 'wewewewewewe43434f-fer0'
        status, _ = pf1.delete_pet(get_key, pet_id)
        assert status == 200
