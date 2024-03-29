import requests
from Auth import base_url, token


class Employee:
    comp_id: str
    api_method = 'employee'

    def __init__(self, comp_id):
        self.comp_id = comp_id  # Запоминаем id компании с которой будем работать

    def get(self, id):  # Получаем данные по id сотрудника
        responce = requests.get(base_url + self.api_method + '/' + str(id))
        assert responce.status_code == 200, responce.json()
        return responce.json()

    def list(self):  # Получаем список с данными всех сотрудников
        responce = requests.get(base_url + self.api_method, params={'company': self.comp_id})
        assert responce.status_code == 200, responce.json()
        return responce.json()

    def new(self, firstName, lastName, middleName, email, url, phone, birthdate, isActive=True):  # Новый сотрудник
        schema = locals()
        schema.pop('self')
        schema['phone'] = str(phone).replace('+', '').replace(' ', '')
        schema['companyId'] = int(self.comp_id)
        responce = requests.post(base_url + self.api_method, headers=token(), json=schema)
        assert responce.status_code == 201, responce.json()
        return responce.json()

    def edit(self, id, firstName, lastName, middleName, email, url, phone, birthdate, isActive=True):  # Редактируем сотрудника
        schema = locals()
        schema.pop('self')
        schema['phone'] = str(phone).replace('+', '').replace(' ', '')
        responce = requests.patch(base_url + self.api_method + '/' + str(id), headers=token(), json=schema)
        assert responce.status_code == 200, responce.json()
        return responce.json()
