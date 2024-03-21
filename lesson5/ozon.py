from selenium.webdriver.common.by import By
from time import sleep
from driver import driver  # выбор браузера для всех моих тестов в файле driver.py


driver.get('https://www.ozon.ru/')
sleep(10)
all_button = driver.find_element(By.XPATH, '(//*[contains(concat(" ", normalize-space(@class), " "), "search-bar-wrapper")]/*/*/*)[1]')
all_button.click()
sleep(10)
driver.quit()
