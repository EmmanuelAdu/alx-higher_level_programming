#!/usr/bin/python3
"""Define the function"""


def matrix_divided(matrix, div):
    """Divide all elements in a matrix

    Args:
          matrix(list) - a list of lists
          div(int or float) - the divisor

    Raises:
           TypeError: If the matrix does not contain either int or float
           TypeError: If matrix contains rows of different size
           TypeError: If div is not a number
           ZeroDivisionError: If div is 0
    """
    if (
            not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                (isinstance(n, float) or isinstance(n, int))
                for n in [num for row in matrix for num in row])
    ):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
