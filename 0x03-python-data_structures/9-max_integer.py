#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return None

    num_max = my_list[0]

    for i in my_list:
        if i > num_max:
            num_max = i
    return num_max
