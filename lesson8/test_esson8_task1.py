import pytest
from Auth import login
from Company import Company
from Employee import Employee

comp_id = Company().list()[-1]['id']  # Берем id последней компании
my_employee = Employee(comp_id)  # Сотрудники этой компании

login('leonardo', 'leads')


@pytest.mark.parametrize(
    ('first_name, last_name, mid_name, email, url, phone, birthdate, is_active'),
    [
        # Позитивные тесты
        ('Иванов', 'Иван', 'Иванович', 'test@test.ru', 'http://test.test', '1234567890', '2000-01-01', True),  # Все поля
        ('First', 'Last', '', 'qwerty@rt.ru', '', '', '2000-01-01', True),  # только обязательные поля
        # Негативные тесты
        pytest.param('', '', '', '', '', '', '', True, marks=pytest.mark.xfail)  # Все пустые поля
    ]
)
def test_new_employee(first_name, last_name, mid_name, email, url, phone, birthdate, is_active):
    e = my_employee.new(first_name, last_name, mid_name, email, url, phone, birthdate, is_active)
    assert e['id'] > 0  # Есть id нового сотрудника (полюбому больше 0)


def test_employee_list():
    e = my_employee.list()
    assert len(e) > 0  # Список присутствует


def test_get_employee():
    id = my_employee.list()[-1]['id']  # Получаем список, берем id последнего сотрудника
    e = my_employee.get(id)
    assert e['id'] == id


@pytest.mark.parametrize(
    ('first_name, last_name, mid_name, email, url, phone, birthdate, is_active'),
    [
        # Позитивные тесты
        ('Иванов', 'Иван', 'Иванович', 'test@test.ru', 'http://test.test', '1234567890', '2000-01-01', True),  # Все поля
        ('', 'Петр', '', 'qwerty@rt.ru', '', '', '', True),  # только обязательные поля
        # Негативные тесты
        pytest.param('', '', '', '', '', '', '', True, marks=pytest.mark.xfail)  # Все пустые поля
    ]
)
def test_edit_employee(first_name, last_name, mid_name, email, url, phone, birthdate, is_active):
    id = my_employee.list()[-1]['id']
    e = my_employee.edit(id, first_name, last_name, mid_name, email, url, phone, birthdate, is_active)
    assert e['id'] == id  # Вернулся id отредактированного сотрудника
