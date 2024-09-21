import pytest
from brackets import check_brackets

@pytest.mark.parametrize(
        'string,expected',
        (
            ('(((([{}]))))', True),
            ('[([])((([[[]]])))]{()}', True),
            ('{{[()]}}', True),
            ('}{}', False),
            ('{{[(])]}}', False),
            ('[[{())}]', False)
        )
)
def test_check_brackets(string:str, expected:bool):
    assert check_brackets(string) == expected
