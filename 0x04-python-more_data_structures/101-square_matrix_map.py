#!/usr/bin/python3
'''This function compute square value of integers of a matrix using map'''


def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
