def FizzBuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return 'FizzBuzz'
        return 'Fizz'
    if is_multiple(value, 5):
        return 'Buzz'
    return str(value)

def is_multiple(value, mod):
    return (value % mod) == 0

