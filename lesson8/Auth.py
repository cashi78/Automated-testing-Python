import requests

# тут храним общее для всех...
base_url = 'https://x-clients-be.onrender.com/'
x_client_token = ''


def token():
    return x_client_token


# ...и метод для авторизации
def login(name, pswd):
    global x_client_token
    s = requests.post(base_url + 'auth/login', json={'username': name, 'password': pswd})
    assert s.status_code == 201
    x_client_token = s.json()['userToken']  # запоминаем токен для дальнейшей работы
