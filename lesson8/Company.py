import requests
from Auth import base_url


# Весь класс здесь описывать не будем, в задании у нас работа только с Employee,
# но один метод нам понадобится
class Company:

    def list(self):
        return requests.get(base_url + 'company').json()
