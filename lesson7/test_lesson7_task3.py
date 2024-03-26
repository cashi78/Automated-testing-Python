from driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from SaucePage import SaucePage


def test_sauce():
    driver.get('https://www.saucedemo.com/')
    sauce_page = SaucePage()
    sauce_page.login('standard_user', 'secret_sauce')
    sauce_page.add_item('Sauce Labs Backpack')
    sauce_page.add_item('Sauce Labs Bolt T-Shirt')
    sauce_page.add_item('Sauce Labs Onesie')
    sauce_page.open_cart()
    sauce_page.check_out()
    sauce_page.fill_form('Василий', 'Петров', '600000')
    sauce_page.do_continue()
    total = sauce_page.cart_total()
    driver.quit()
    assert total == '$58.29'
