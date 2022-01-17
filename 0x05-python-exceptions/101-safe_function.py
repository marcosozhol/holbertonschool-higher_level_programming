#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        _return = fct(*args)
        return _return
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
