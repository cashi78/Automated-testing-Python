from driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
waiter = WebDriverWait(driver, 30)
waiter.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, '#spinner')))  # Ждем ухода спиннера )
src = driver.find_elements(By.CSS_SELECTOR, '#image-container img')[2]  # [2] - это третий )

print(src.get_dom_attribute('src'))
driver.quit()
