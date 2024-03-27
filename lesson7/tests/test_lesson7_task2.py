import sys
sys.path[0] = '\\'.join(sys.path[0].split('\\')[:-1])
from tests.driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from pages.CalcPage import CalcPage


def test_calc():
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    calc_page = CalcPage()
    calc_page.set_delay(45)
    calc_page.calculate('7+8=')
    calc_page.wait()
    assert calc_page.screen() == 15
#   driver.quit() # он нам нужен в следующем тесте
