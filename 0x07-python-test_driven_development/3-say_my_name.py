#!/usr/bin/python3
""" 
This module supplies one function, say_my_name(). For example,
>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last name>"
    checks if first_name is a string
    checks if last_name is a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
