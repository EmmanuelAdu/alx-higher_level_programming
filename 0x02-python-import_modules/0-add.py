#!/usr/bin/python3
'''This file imports another file and executes it '''


if __name__ == "__main__":
    from add_0 import add

    x = 1
    y = 2
    print("{} + {} = {}".format(x, y, add(x, y)))
