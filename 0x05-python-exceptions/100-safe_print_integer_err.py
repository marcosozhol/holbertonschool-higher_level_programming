#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
        return True
    except TypeError as error:
        print('Exception: {})'.format(error), file=sys.stderr)
        return False
    except ValueError as error_1:
        print('Exception: {}'.format(error_1), file=sys.stderr)
        return False
