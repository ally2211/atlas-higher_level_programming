#!/usr/bin/python3


def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return set1, set2

    common = []
    for element in set_1:
        if element in set_2:
            common.append(element)
    return common
