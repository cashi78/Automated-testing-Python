from selenium.webdriver.common.by import By
from time import sleep
from driver import driver  # выбор браузера для всех моих тестов в файле driver.py


driver.get('http://the-internet.herokuapp.com/login')
sleep(3)
username = driver.find_element(By.CSS_SELECTOR, '#username')
password = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
username.send_keys('tomsmith')
password.send_keys('SuperSecretPassword!')
sleep(3)
submit.click()
sleep(10)
driver.quit()
