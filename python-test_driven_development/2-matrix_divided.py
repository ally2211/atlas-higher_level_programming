#!/usr/bin/python3
"""
Module Documentation:  This module takes a matrix and divides by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
              raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rowlen = len(matrix[0])

    for row in matrix:
        if len(row) != rowlen:
          raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
