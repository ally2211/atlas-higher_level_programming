#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        return
    """
    new_list = []
    for element in my_list:
        new_list.append(element * number)
    return new_list
    """
    return list(map(lambda x: x * number, my_list))
