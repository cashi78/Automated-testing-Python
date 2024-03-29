import requests

# тут храним общее для всех...
base_url = 'https://x-clients-be.onrender.com/'
token_header = {}


def token():
    return token_header


# ...и метод для авторизации
def login(name, pswd):
    global token_header
    s = requests.post(base_url + 'auth/login', json={'username': name, 'password': pswd})
    assert s.status_code == 201
    token_header['x-client-token'] = s.json()['userToken']  # запоминаем токен для дальнейшей работы
    pass
