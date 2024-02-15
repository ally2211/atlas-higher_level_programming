#!/usr/bin/python3
"""
Module Doc:  returns pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        # Each element in the middle of the row is theiuhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyhjyj
        # sum of the two elements above it
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
    """
    triangle = []
    for row in range(n):
        layer = []
        for column in range(row + 1):
            if (column > 0 and column < row and row > 0):
                #add previous and current column from previous row
                layer.append(triangle[row - 1][column - 1] + triangle[row - 1][column])
            else:
                layer.append(1)
        triangle.append(layer)
    return triangle

"""print(pascals_triangle(5))"""