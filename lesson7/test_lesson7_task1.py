from driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from MainPage import MainPage


def test_form():
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    main_page = MainPage()
    main_page.set_fields(['Иван', 'Петров', 'Ленина, 55-3', '', 'Москва', 'Россия', 'test@skypro.com', '+7985899998787', 'QA', 'SkyPro'])
    main_page.submit()

    assert main_page.is_red('zip-code')

    for f in main_page.fields:
        if f != 'zip-code':
            assert main_page.is_green(f)
#   driver.quit() # он нам нужен в следующем тесте
