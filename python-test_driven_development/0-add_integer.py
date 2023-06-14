#!/usr/bin/python3
'''
is a funtion that recive two integer and return the add
'''


def add_integer(a, b=98):
    ''' this is a funtion that recive two integer
    args:
        a(int) : is a number, b(int) : is a number
    return:
        return an integer: addicion of a and b'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
