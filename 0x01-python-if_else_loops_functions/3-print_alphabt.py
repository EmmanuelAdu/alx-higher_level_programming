#!/usr/bin/python3
'''This program prints lowercase except q and e'''
for lowercase in range(97, 123):
    if chr(lowercase) != 'e' and chr(lowercase) != 'q':
        print("{}".format(chr(lowercase)), end="")
