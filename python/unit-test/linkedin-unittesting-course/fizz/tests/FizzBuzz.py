
def FizzBuzz(value):
    """
    Function will return the string Fizz if the passed in number is a multiple of three,
    Buzz if the passed in number is a multiple of five, and
    FizzBuzz if the passed in number is a multiple of three and five

    :param value:
    :return:
    """
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return 'FizzBuzz'
        return 'Fizz'
    if is_multiple(value, 5):
        return 'Buzz'
    return str(value)


def is_multiple(value, mod):
    return (value % mod) == 0

