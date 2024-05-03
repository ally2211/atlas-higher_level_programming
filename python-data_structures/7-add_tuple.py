#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Extend both tuples to be of length 2
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add the corresponding elements of the tuples
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple
