from driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from selenium.webdriver.common.by import By

driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()
print(button.text)
driver.quit()
