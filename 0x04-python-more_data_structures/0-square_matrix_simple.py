#!/usr/bin/python3
'''This function computes the square of int in a matrix'''


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_element = col ** 2
            new_row.append(new_element)
        new_matrix.append(new_row)
    return (new_matrix)
