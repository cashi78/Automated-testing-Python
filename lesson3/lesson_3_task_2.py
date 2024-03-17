from smartphone import Smartphone
from mimesis import Hardware, Person  # библиотека для генерац. тестовых данных

catalog = []
phone = Hardware()  # Класс для генерации железа, в т.ч. названий мобилок
person = Person('ru')  # Класс для генерации персон. данных

# Создаем, заполняем...
for x in range(0, 5):
    s = phone.phone_model().split(" ", 1)  # эта зараза генерит одной строкой)
    brand = s[0]  # ...распарсим  на брэнд...
    model = s[1]  # ...и модель
    catalog.append(Smartphone(brand, model, person.phone_number()))

# Печатаем...
for x in catalog:
    print(x.brand_name, x.model_name, x.phone_number)
