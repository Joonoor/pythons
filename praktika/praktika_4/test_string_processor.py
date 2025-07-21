import pytest  # type: ignore
from string_processor import StringProcessor


test_str = StringProcessor()

# res = test_str.process("galya")
# assert res == "Galya."


# def test_str_text1():
#    test_str = StringProcessor()
# res = test_str.process('galya')
# assert res == "Galya."

@pytest.mark.parametrize("text, result", [('galya', 'Galya.'),
                                          ('Galya', 'Galya.'),
                                          ('galya.', 'Galya.')])
def test_process_positive(text, result):
    test_str = StringProcessor()
    res = test_str.process(text)
    assert res == result


@pytest.mark.parametrize("text, result", [('', '.'),
                                          ('   ', '   .')])
def test_process_negative(text, result):
    test_str = StringProcessor()
    res = test_str.process(text)
    assert res == result
