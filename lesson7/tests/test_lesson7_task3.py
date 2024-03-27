import sys
sys.path[0] = '\\'.join(sys.path[0].split('\\')[:-1])
from tests.driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from pages.SaucePage import SaucePage
from faker import Faker

items_to_find = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']  # Список чего поискать


def test_sauce():
    driver.get('https://www.saucedemo.com/')
    sauce_page = SaucePage()
    sauce_page.login('standard_user', 'secret_sauce')
    for i in items_to_find:
        sauce_page.add_item(i)
    sauce_page.open_cart()
    sauce_page.check_out()
    fake = Faker('ru_RU')
    sauce_page.fill_form(fake.first_name(), fake.last_name(), fake.postcode())
    sauce_page.do_continue()
    total = sauce_page.cart_total()
    driver.quit()
    assert total == '$58.29'
