#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 123:  # recorre abc en min en ascii
        return True
    else:
        return False
