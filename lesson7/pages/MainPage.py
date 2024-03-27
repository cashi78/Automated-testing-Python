from tests.driver import driver
from selenium.webdriver.common.by import By


class MainPage:

    fields = ['first-name', 'last-name', 'address', 'zip-code', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
    green = 'alert-success'
    red = 'alert-danger'

    def set_field(self, field, value):
        driver.find_element(By.CSS_SELECTOR, '[name="' + field + '"]').send_keys(value)

    def get_field(self, field):
        return driver.find_element(By.CSS_SELECTOR, '#' + field)

    def set_fields(self, values):
        for i in range(0, len(values)):
            self.set_field(self.fields[i], values[i])

    def submit(self):
        driver.find_element(By.CSS_SELECTOR, '[type=submit]').click()

    def is_red(self, field):
        return self.get_field(field).get_attribute('class').find(self.red) > -1

    def is_green(self, field):
        return self.get_field(field).get_attribute('class').find(self.green) > -1
