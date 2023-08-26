#!/usr/bin/python3
'''This function returns the length and first char of a tuple'''


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
