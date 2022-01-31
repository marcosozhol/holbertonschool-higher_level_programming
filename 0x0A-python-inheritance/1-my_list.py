#!/usr/bin/python3
""" Task for print_sorted """


class MyList(list):
    """ Class MyList that inherits from list """

    def print_sorted(self):
        """ sorted list """
        print(sorted(self))
