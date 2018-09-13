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
    """
    Use cases:
    - Can I call FizzBuzz
    - Get "1" when I pass in 1
    - Get "2" when I pass in 2
    - Get "Fizz" when I pass in 3
    - Get "Buzz" when I pass in 5
    - Get "Fizz" when I pass in 6 (a multiple of 3)
    - Get "Buzz" when I pass in 10 (a multiple of 5)
    - Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)

    :param input:
    :param expected:
    :return:
    """
    value = FizzBuzz(input)
    assert value == expected
