#!/usr/bin/python3
'''This function prints an int with {:d} format'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
