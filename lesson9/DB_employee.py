from sqlalchemy import create_engine
from sqlalchemy.sql import text


def kstr(keys):
    return ', '.join(list(keys))


def vstr(values):
    return str(list(values))[1:-1]


def fields_eq_values(schema):
    return ', '.join([i[1:].replace('\':', ' =') for i in str(schema)[1:-1].split(', ')])


dbcs = 'postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet'
db = create_engine(dbcs)


class DB_employee:
    comp_id: str

    def __init__(self, comp_id):
        self.comp_id = comp_id  # Запоминаем id компании с которой будем работать

    def get(self, _id):  # Получаем данные по id сотрудника
        return db.execute('select * from employee where company_id = :comp_id and id = :id', id=_id, comp_id=self.comp_id).fetchall()

    def list(self):  # Получаем список с данными всех сотрудников
        return db.execute(text('select * from employee where company_id = :comp_id'), comp_id=self.comp_id).fetchall()

    def new(self, first_name, last_name, middle_name, email, avatar_url, phone, birthdate, is_active=True):  # Новый сотрудник
        schema = locals()
        schema.pop('self')
        schema['phone'] = str(phone).replace('+', '').replace(' ', '')
        schema['company_id'] = int(self.comp_id)
        query = 'insert into employee (:fields) values (:values) returning id'
        res = db.execute(query.replace(':fields', kstr(schema.keys())).replace(':values', vstr(schema.values())))
        assert res.rowcount == 1
        return res.fetchall()[0][0]

    def edit(self, _id, first_name, last_name, middle_name, email, avatar_url, phone, birthdate, is_active=True):  # Редактируем сотрудника
        schema = locals()
        schema.pop('self')
        schema.pop('_id')
        schema['phone'] = str(phone).replace('+', '').replace(' ', '')
        query = 'update employee set :fields where id = :id returning *'
        res = db.execute(text(query.replace(':fields', fields_eq_values(schema))), id=_id)
        assert res.rowcount == 1
        return res.fetchall()

    def delete(self, _id):
        query = 'delete from employee where id = :id'
        res = db.execute(text(query), id=_id).rowcount
        assert res == 1
        return res
