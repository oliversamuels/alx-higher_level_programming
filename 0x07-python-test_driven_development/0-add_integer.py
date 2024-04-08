#!/usr/bin/python3
"""
This module supplies one function, add_integer(). For example, 
>>> add_integer(5, 10)
15
"""


def add_integer(a, b=98):
    """
    Checks if int, otherwise return sum
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
