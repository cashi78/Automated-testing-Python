import sys
sys.path[0] = '\\'.join(sys.path[0].split('\\')[:-1])
from tests.driver import driver  # выбор браузера для всех моих тестов в файле driver.py
from pages.MainPage import MainPage
from faker import Faker


def test_form():
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    main_page = MainPage()
    fake = Faker('ru_RU')
    main_page.set_fields(
        [
            fake.first_name(),
            fake.last_name(),
            fake.street_address(),
            '',
            fake.city(),
            fake.country(),
            fake.ascii_email(),
            fake.phone_number(),
            fake.job(),
            fake.company()
        ]
    )

    main_page.submit()
    assert main_page.is_red('zip-code')

    for f in main_page.fields:
        if f != 'zip-code':
            assert main_page.is_green(f)
#   driver.quit() # он нам нужен в следующем тесте
