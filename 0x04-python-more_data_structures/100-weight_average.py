#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0

    w = 0
    we = 0
    for i in my_list:
        w += i[1]
        we += i[0] * i[1]
    return we / w
