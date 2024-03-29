import pytest
from faker import Faker
from Auth import login
from Company import Company
from Employee import Employee


login('raphael', 'cool-but-crude')

c = Company()
for i in c.list():
    pass  # c.del_company(i['id'])  # Когда нужно вручную почистить за собой после упавших тестов

fake = Faker('ru_RU')


@pytest.mark.parametrize(
    ('first_name, last_name, mid_name, email, url, phone, birthdate, is_active'),
    [
        # Позитивные тесты
        (fake.first_name(), fake.last_name(), fake.middle_name(), fake.ascii_email(), fake.url(), fake.phone_number(), fake.date(), fake.boolean()),  # Все поля
        (fake.first_name(), fake.last_name(), '', fake.ascii_email(), '', '', fake.date(), fake.boolean()),  # только обязательные поля
        # Негативные тесты
        pytest.param('', '', '', '', '', '', '', fake.boolean(), marks=pytest.mark.xfail)  # Все пустые поля
    ]
)
def test_new_employee(first_name, last_name, mid_name, email, url, phone, birthdate, is_active):
    comp_id = Company().add_company(fake.company(), fake.catch_phrase())  # Добавляем компанию и берем ее id
    my_employee = Employee(comp_id)
    emp_count_before = len(my_employee.list())  # Было сотрудников ДО
    my_employee.new(first_name, last_name, mid_name, email, url, phone, birthdate, is_active)
    emp_count_after = len(my_employee.list())  # Стало сотрудников после
    Company().del_company(comp_id)  # Удаляем за собой
    assert emp_count_before + 1 == emp_count_after


@pytest.mark.parametrize(
    'count',
    [
        5
    ]
)
def test_employee_list(count):
    comp_id = Company().add_company(fake.company(), fake.catch_phrase())  # Добавляем компанию и берем ее id
    my_employee = Employee(comp_id)
    emp_count_before = len(my_employee.list())  # Было сотрудников ДО

    for i in range(0, count):
        my_employee.new(fake.first_name(), fake.last_name(), fake.middle_name(), fake.ascii_email(), fake.url(), fake.phone_number(), fake.date(), fake.boolean())

    emp_count_after = len(my_employee.list())  # Стало сотрудников после
    Company().del_company(comp_id)  # Удаляем за собой
    assert emp_count_before + count == emp_count_after  # Проверяем что все добавились


def test_get_employee():
    comp_id = Company().add_company(fake.company(), fake.catch_phrase())  # Добавляем компанию и берем ее id
    my_employee = Employee(comp_id)
    my_employee.new(fake.first_name(), fake.last_name(), fake.middle_name(), fake.ascii_email(), fake.url(), fake.phone_number(), fake.date(), fake.boolean())
    id = my_employee.list()[-1]['id']  # Получаем список, берем id последнего сотрудника
    e = my_employee.get(id)
    Company().del_company(comp_id)  # Удаляем за собой
    assert e['id'] == id  # Что просили, то и получили?


@pytest.mark.parametrize(
    ('first_name, last_name, mid_name, email, url, phone, birthdate, is_active'),
    [
        # Позитивные тесты
        (fake.first_name(), fake.last_name(), fake.middle_name(), fake.ascii_email(), fake.url(), fake.phone_number(), fake.date(), fake.boolean()),  # Все поля
        (fake.first_name(), fake.last_name(), '', fake.ascii_email(), '', '', fake.date(), fake.boolean()),  # только обязательные поля
        # Негативные тесты
        pytest.param('', '', '', '', '', '', '', fake.boolean(), marks=pytest.mark.xfail)  # Все пустые поля
    ]
)
def test_edit_employee(first_name, last_name, mid_name, email, url, phone, birthdate, is_active):
    comp_id = Company().add_company(fake.company(), fake.catch_phrase())  # Добавляем компанию и берем ее id
    my_employee = Employee(comp_id)
    id = my_employee.new(fake.first_name(), fake.last_name(), fake.middle_name(), fake.ascii_email(), fake.url(), fake.phone_number(), fake.date(), fake.boolean())['id']  # Создаем сотрудника
    edit_id = my_employee.edit(id, first_name, last_name, mid_name, email, url, phone, birthdate, is_active)['id']
    Company().del_company(comp_id)  # Удаляем за собой
    assert edit_id == id  # Вернулся id отредактированного сотрудника
