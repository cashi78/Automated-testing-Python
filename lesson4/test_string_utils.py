import pytest
from string_utils import StringUtils


s = StringUtils()


@pytest.mark.parametrize(
    ('str_in, str_out'),
    [
        # Позитивные тесты
        ('кириллица', 'Кириллица'),  # Кириллица
        ('latin', 'Latin'),  # Латиница
        ('', ''),  # Пустая строка, почему бы нет?
        ('123', '123'),  # числа строкового типа, почему бы нет?
        # Негативные тесты
        pytest.param(123, 123, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_capitalize(str_in, str_out):
    assert str_out == s.capitilize(str_in)


@pytest.mark.parametrize(
    ('str_in, str_out'),
    [
        # Позитивные тесты
        (' кириллица', 'кириллица'),  # Кириллица
        (' latin', 'latin'),  # Латиница
        ('', ''),  # Пустая строка, почему бы нет?
        (' 123', '123'),  # числа строкового типа, почему бы нет?
        # Негативные тесты
        pytest.param(123, 123, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_trim(str_in, str_out):
    assert str_out == s.trim(str_in)


@pytest.mark.parametrize(
    ('str_in, list_out'),
    [
        # Позитивные
        ('a,b,c', ['a', 'b', 'c']),  # Латиница
        ('а,б,в', ['а', 'б', 'в']),  # Кириллица
        ('1, 2, 3', ['1', '2', '3']),  # с пробелами после разделителя
        ('', []),  # Пустая строка - пустой список, все ок
        # Негативные тесты
        pytest.param(123, [1, 2, 3], marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_to_list(str_in, list_out):
    assert list_out == s.to_list(str_in)


@pytest.mark.parametrize(
    ('string, substr'),
    [
        # Позитивные
        ('Максим', 'си'),  # Кириллица
        ('Maxim', 'xi'),  # Латиница
        ('Pink Floyd', ' F'),  # с пробелами
        ('123456', '34'),  # числа строкового типа
        # Негативные тесты
        pytest.param(123, 123, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_contains(string, substr):
    assert s.contains(string, substr)


@pytest.mark.parametrize(
    ('string, substr, result'),
    [
        ('автотест', 'авто', 'тест'),  # Кириллица
        ('Maxim', 'M', 'axim'),  # Латиница
        ('123456', '34', '1256'),  # числа строкового типа
        ('abcd', 'xyz', 'abcd'),  # ищем то, чего нет
        # Негативные тесты
        pytest.param(123, 123, 123, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, None, marks=pytest.mark.xfail)  # Ничего

    ]
)
def test_delete_symbol(string, substr, result):
    assert result == s.delete_symbol(string, substr)


@pytest.mark.parametrize(
    ('string, substr'),
    [
        # Позитивные
        ('Максим', 'М'),  # Кириллица
        ('John', 'Jo'),  # Латиница
        ('Pink Floyd', 'P'),  # с пробелами
        ('123456', '12'),  # числа строкового типа
        # Негативные тесты
        pytest.param(123, 12, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_starts_with(string, substr):
    assert s.starts_with(string, substr)


@pytest.mark.parametrize(
    ('string, substr'),
    [
        # Позитивные
        ('Максим', 'им'),  # Кириллица
        ('John', 'n'),  # Латиница
        ('Pink Floyd', 'd'),  # с пробелами
        ('123456', '56'),  # числа строкового типа
        # Негативные тесты
        pytest.param(123, 23, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_end_with(string, substr):
    assert s.end_with(string, substr)


@pytest.mark.parametrize(
    ('string, result'),
    [
        # Позитивные
        ('', True),  # Пусто
        (' ', False),  # 1 пробел
        ('Максим', False),  # Кириллица
        ('John', False),  # Латиница
        ('Pink Floyd', False),  # с пробелами
        ('123456', False),  # числа строкового типа
        # Негативные тесты
        pytest.param(0, True, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, True, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_is_empty(string, result):
    assert result == s.is_empty(string)


@pytest.mark.parametrize(
    ('list', 'result'),
    [
        # Позитивные
        (['a', 'b', 'c'], 'a, b, c'),  # Латиница
        (['а', 'б', 'в'], 'а, б, в'),  # Кириллица
        (['1', '2', '3'], '1, 2, 3'),  # с пробелами после разделителя
        ([], ''),  # Пустой список - пустая строка, все ок
        # Негативные тесты
        pytest.param([1, 2, 3], 123, marks=pytest.mark.xfail),  # Числовой тип
        pytest.param(None, None, marks=pytest.mark.xfail)  # Ничего
    ]
)
def test_list_to_string(list, result):
    assert result == s.list_to_string(list)
