from selenium.webdriver.common.by import By
from time import sleep
from driver import driver  # выбор браузера для всех моих тестов в файле driver.py


driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(3)
# driver.find_element(By.CSS_SELECTOR, '.modal-footer').click() # вариант 1
driver.find_element(By.XPATH, "//*[text()='Close']").click()   # вариант 2
sleep(10)
driver.quit()
