#!/usr/bin/python3
def print_last_digit(number):
    last_value = abs(number) % 10
    if number < 0:
        last_value = -last_value
        return last_value
    return last_value
