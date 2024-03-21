from selenium.webdriver.common.by import By
from time import sleep
from driver import driver  # выбор браузера для всех моих тестов в файле driver.py


driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
add_button = driver.find_element(By.XPATH, '//button[contains(text(),"Add Element")]')

for x in range(0, 5):
    add_button.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(len(delete_buttons))
sleep(10)
driver.quit()
