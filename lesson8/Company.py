import requests
from Auth import base_url, token


# Весь класс здесь описывать не будем, в задании у нас работа только с Employee,
# но пару методов нам понадобится
class Company:

    api_method = 'company'

    def list(self):
        return requests.get(base_url + self.api_method).json()

    def add_company(self, name, descr):
        schema = {
            "name": name,
            "description": descr
        }
        responce = requests.post(base_url + self.api_method, headers=token(), json=schema)
        assert responce.status_code == 201, responce.json()
        return responce.json()['id']

    def del_company(self, id):
        responce = requests.get(base_url + self.api_method + '/delete/' + str(id), headers=token())
        assert responce.status_code == 200, responce.json()
        return responce.json()['id']
