from DB_employee import DB_employee
my_db_employee = DB_employee('3555')
emp_id = int


def test_new_emp():
    global emp_id
    emp_id = my_db_employee.new('first_name', 'last_name', 'mid_name', 'email', 'url', '1234567890', '2000-01-01', True)
    print('NEW:', emp_id)


def test_list_emp():
    res = my_db_employee.list()
    print('LIST:', res)


def test_edit_emp():
    res = my_db_employee.edit(emp_id, 'UPDATED', 'UPDATED', 'mid_name', 'email', 'url', '1234567890', '2000-01-01', True)
    print('EDIT:', res)


def test_del_emp():
    res = my_db_employee.delete(emp_id)
    print('DELETE:', res)
