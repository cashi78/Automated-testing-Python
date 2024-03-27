from tests.driver import driver
from selenium.webdriver.common.by import By


class SaucePage:

    def login(self, login, psw):
        driver.find_element(By.ID, 'user-name').send_keys(login)
        driver.find_element(By.ID, 'password').send_keys(psw)
        driver.find_element(By.ID, 'login-button').click()

    def add_item(self, text):
        s = driver.find_elements(By.CSS_SELECTOR, '.inventory_item')
        for i in s:
            if i.find_element(By.CSS_SELECTOR, '.inventory_item_name').text == text:
                i.find_element(By.CSS_SELECTOR, '.btn_inventory').click()

    def open_cart(self):
        driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    def check_out(self):
        driver.find_element(By.CSS_SELECTOR, '.checkout_button').click()

    def fill_form(self, first_name, last_name, postal_code):
        driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)

    def do_continue(self):
        driver.find_element(By.CSS_SELECTOR, '.submit-button').click()

    def cart_total(self):
        return driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text.split(' ')[1]
