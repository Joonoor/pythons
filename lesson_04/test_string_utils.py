import pytest  # type: ignore
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("Галя", "Галя"),
    ("гАЛЯ", "Галя"),
    ("ГАЛЯ", "Галя")])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (",!?%", ",!?%")])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" galya", "galya"),
    ("    galya", "galya"),
    ("galya", "galya"),
    (" !aylag", "!aylag")])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("galya ", "galya "),
    ("ga lya", "ga lya")])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Galya", "Ga", True),
    ("galya", "g", True),
    (" galya", " ", True),
    ("galya.", ".", True),
    ("galya!", "!", True),
    ("galya%", "%", True)
    ])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Galya", "B", False)])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Galya", "G", "alya"),
    ("galya", "g", "alya"),
    ("galya1", "1", "galya"),
    ("galya!", "!", "galya"),
    ("galya%", "%", "galya")])
def test_delete_simbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Galya", "B", "Galya")])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
