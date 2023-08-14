#!/usr/bin/python3
'''This function prints a matrix of integers'''


def print_matrix_integer(matrix=[[]]):
    for hori in matrix:
        for vert in hori:
            print("{:d}".format(vert), end=" "if vert != hori[-1] else "")
        print()
