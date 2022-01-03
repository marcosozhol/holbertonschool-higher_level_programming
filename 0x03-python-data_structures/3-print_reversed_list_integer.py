#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = my_list[-1::-1]

    if my_list:
        for n in range(len(rev)):
            print("{:d}".format(rev[n]))
