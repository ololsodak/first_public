import json
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder # для постинга различных типов данных (фото)


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/' # базовый УРЛ при инициализации класса

    def get_api_key(self, email: str, password: str) -> json:
        '''метод запроса ключа'''
        # данные передаются в заголовке
        headers = {
            'email': email,
            'password': password
        }
        # отправляем запрос
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text

        return status, result
    # метод запроса списка животных
    def get_list_of_pets(self, auth_key: str, filter: str) -> json:
        '''Метод делает запрос на сервер и возвращает список животных в зависимости
        от фильтра(всех или пользотеля)'''
        headers = {
            'auth_key': auth_key['key']
        }
        # параметр
        filter = {
            'filter': filter
        }
    # формируем запрос
        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text

        return status, result

    def post_new_pet_with_photo(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        '''Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца'''
        data= MultipartEncoder(
            fields={
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
        headers ={'auth_key': auth_key['key'], 'Content-type': data.content_type}
        res = requests.post(self.base_url+'/api/pets', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        '''Метод отправляет (постит) на сервер данные о питомце, которого нужно удалить, и возвращает статус
        запроса на сервер и результат в формате JSON с данными удаленного питомца'''
        headers = {'auth_key':auth_key['key']}

        res = requests.delete(self.base_url+'api/pets/'+ pet_id, headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text
        print(result)
        return status, result

    def put_info_of_pet(self,auth_key: json, pet_id: str, name: str, animal_type: str, age: str) -> json:
        '''Метод отправляет (постит) на сервер данные о питомце, которые нужно изменить, и возвращает статус
            запроса на сервер и результат в формате JSON с данными питомца'''
        headers = {
            'auth_key':auth_key['key']
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.put(self.base_url+'api/pets/'+pet_id, headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text
        print(result)
        return status, result

# Задание 19.7.2. Два нереализованных метода
    # 1
    def post_new_pet_without_photo(self, auth_key: str, name: str, anymal_type: str, age: str ) -> json:
        '''Метод отправляет (постит) на сервер данные о добавляемом питомце (без фото)
           и возвращает статус запроса на сервер и результат в формате JSON с данными добавленного питомца'''
        # ключ передается в заголовке
        headers = {'auth_key': auth_key['key']}
        # данные передаются в data
        data = {
            'name': name,
            'animal_type': anymal_type,
            'age': age
        }
        # запрос на сервер
        res = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text
        print(result)
        return status, result

    #2
    def set_photo_to_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        '''Метод отправляет (постит) на сервер фото питомца
        и возвращает статус запроса на сервер и результат в формате JSON с данными питомца
        Но с результатом на данный момент емть баг, он не возвращает данные в json-формате'''
        data = MultipartEncoder(
            fields={
                  'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
                  })
        headers = {'auth_key': auth_key['key'], 'Content-type': data.content_type}
        res = requests.post(self.base_url+'/api/pets/set_photo/'+pet_id, headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError as e:
            result = res.text
        print(result)
        return status, result