import requests
from Auth import base_url, token


class Employee:
    comp_id: str

    def __init__(self, comp_id):
        self.comp_id = comp_id  # Запоминаем id компании с которой будем работать

    def get(self, id):  # Получаем данные по id сотрудника
        responce = requests.get(base_url + 'employee/' + str(id))
        assert responce.status_code == 200
        return responce.json()

    def list(self):  # Получаем список с данными всех сотрудников
        responce = requests.get(base_url + 'employee', params={'company': self.comp_id})
        assert responce.status_code == 200
        return responce.json()

    def new(self, first_name, last_name, mid_name, email, url, phone, birthdate, is_active=True):  # Новый сотрудник
        schema = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": mid_name,
            "companyId": int(self.comp_id),
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": is_active
        }
        responce = requests.post(base_url + 'employee', headers={'x-client-token': token()}, json=schema)
        # print(' NEW ', responce.status_code)
        assert responce.status_code == 201
        return responce.json()

    def edit(self, id, first_name, last_name, mid_name, email, url, phone, birthdate, is_active=True):  # Редактируем сотрудника
        schema = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": mid_name,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": is_active
        }
        responce = requests.patch(base_url + 'employee/' + str(id), headers={'x-client-token': token()}, json=schema)
        # print(' EDIT ', responce.status_code)
        assert responce.status_code == 200
        return responce.json()
