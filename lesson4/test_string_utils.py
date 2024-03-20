import pytest
from string_utils import StringUtils


s = StringUtils()


@pytest.mark.parametrize('str_in, str_out', [('abc', 'Abc'), ('абв', 'Абв')])
def test_capitalize(str_in, str_out):
    assert str_out == s.capitilize(str_in)


@pytest.mark.parametrize('str_in, str_out', [(' abc', 'abc'), (' абв', 'абв')])
def test_trim(str_in, str_out):
    assert str_out == s.trim(str_in)


@pytest.mark.parametrize('str_in, list_out', [('a,b,c', ['a', 'b', 'c']), ('а,б,в', ['а', 'б', 'в'])])
def test_to_list(str_in, list_out):
    assert list_out == s.to_list(str_in)


@pytest.mark.parametrize('string, substr', [('Igor', 'go'), ('Maxim', 'xi')])
def test_contains(string, substr):
    assert s.contains(string, substr)


@pytest.mark.parametrize('string, substr, result', [('Igor', 'Ig', 'or'), ('Maxim', 'M', 'axim')])
def test_delete_symbol(string, substr, result):
    assert result == s.delete_symbol(string, substr)


@pytest.mark.parametrize('string, substr', [('Igor', 'Ig'), ('Maxim', 'M')])
def test_starts_with(string, substr):
    assert s.starts_with(string, substr)


@pytest.mark.parametrize('string, substr', [('Igor', 'or'), ('Maxim', 'm')])
def test_end_with(string, substr):
    assert s.end_with(string, substr)


@pytest.mark.parametrize('string', ['', ' ', '   ', ''])
def test_is_empty(string):
    assert s.is_empty(string)


@pytest.mark.parametrize('list, result', [(['a', 'b', 'c'], 'a, b, c'), (['а', 'б', 'в'], 'а, б, в')])
def test_list_to_string(list, result):
    assert result == s.list_to_string(list)
