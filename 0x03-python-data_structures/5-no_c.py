#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    count = 0
    for index in string_list:
        if index == 'c' or index == 'C':
            string_list[count] = ""
        count += 1
    return "".join(string_list)
