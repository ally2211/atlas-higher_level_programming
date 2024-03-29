#!/usr/bin/python3
"""
This is a module that defines a class add_integer.
However it coverts floats to integers too
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b.
    """

    if not isinstance(a, (float, int)) or a is None or a != a:
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)) or b is None or b != b:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    if result == float('inf') or result == -float('inf'):
        raise OverflowError("result is infinity")
    if result == float('NaN'):
        raise ValueError("cannot convert float NaN to integer")
    return result
