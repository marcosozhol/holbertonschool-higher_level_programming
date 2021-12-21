#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:  # compara rango en ascii
            d = chr(ord(c) - 32)  # d: almacena letra en may restando en ascii
        else:
            d = c
        print("{:s}".format(d), end="")
    print('')
