#!/usr/bin/python3
""" Module to read file """


def read_file(filename=""):
    """ Open file and print """
    with open(filename) as f:
        for line in f:
            print(line, end="")
