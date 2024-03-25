from driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('http://uitestingplayground.com/ajax')
waiter = WebDriverWait(driver, 30)
driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
success = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.bg-success')))  # Ждем появления плашки
print(success.text)
driver.quit()
