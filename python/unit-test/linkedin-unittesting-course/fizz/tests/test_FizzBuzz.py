import pytest
from FizzBuzz import FizzBuzz
@pytest.mark.parametrize('input,expected', [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, 'Fizz'),
    (10, 'Buzz'),
    (15, 'FizzBuzz')
])
def test_validateResult(input, expected):
    value = FizzBuzz(input)
    assert value == expected
