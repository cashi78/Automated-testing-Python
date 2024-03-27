from tests.driver import driver
from selenium.webdriver.common.by import By


class CalcPage:

    def set_delay(self, value):
        driver.execute_script("arguments[0].value = '" + str(value) + "'", driver.find_element(By.ID, 'delay'))

    def press_button(self, b):
        driver.find_element(By.XPATH, '//span[contains(@class, "btn") and contains(text(), "' + b + '")]').click()

    def calculate(self, exp):
        for b in exp:
            self.press_button(b)

    def screen(self):
        return int(driver.find_element(By.CLASS_NAME, 'screen').text)

    def wait(self):
        while (driver.find_element(By.ID, 'spinner').get_attribute('style')) == 'display: inline-block;':
            pass
