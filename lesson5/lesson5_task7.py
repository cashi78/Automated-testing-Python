from selenium.webdriver.common.by import By
from time import sleep
from driver import driver  # выбор браузера для всех моих тестов в файле driver.py


driver.get('http://the-internet.herokuapp.com/inputs')
sleep(3)
input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input.send_keys('1000')
sleep(3)
input.clear()
sleep(2)
input.send_keys('999')
sleep(10)
driver.quit()
