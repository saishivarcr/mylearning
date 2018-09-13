from demo import multiply


def test_check2MultiplyBy3is6():
    result = multiply(2, 3)
    assert result == 6


def test_check2MultiplyBy0is0():
    result = multiply(2, 0)
    assert result == 0