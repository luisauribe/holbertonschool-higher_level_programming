#!/usr/bin/python3
"""This module contain matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: It´s a list of lists of integers or floats.
        div: Number by which the matrix will be divided.
    Raise:
        - TypeError if matrix are not integers or floats.
        - TypeError if div are not integers or floats.
        - TypeError if the rows in the matrix is not the same size.
        - TypeError if the row or row runner is not an integer or a float.
        - ZeroDivisionError if div is equal to 0.
    Return:
        A new Matrix.
    """
    mess = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(matrix, list) or any(type(w) != list for w in matrix):
        raise TypeError(mess)

    if not matrix or any(not row for row in matrix):
        raise TypeError(mess)

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if any(any(not isinstance(j, (int, float)) for j in w)for w in matrix):
        raise TypeError(mess)

    def op(num):
        return(round(num/div, 2))

    new_matrix = []

    for c in matrix:
        new_matrix.append(list(map(op, c)))

    return(new_matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
