#!/usr/bin/python3
'''This function executes a function safely'''
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    return result
