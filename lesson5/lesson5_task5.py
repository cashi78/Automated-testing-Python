from selenium.webdriver.common.by import By
from time import sleep
from driver import driver  # выбор браузера для всех моих тестов в файле driver.py


driver.get('http://uitestingplayground.com/classattr')


for x in range(0, 3):
    button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    sleep(2)
    driver.switch_to.alert.accept()
    # print(button.text)
    driver.refresh()
sleep(10)
driver.quit()
