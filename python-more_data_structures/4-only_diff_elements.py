#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if set_1 is None and  set_2 is None:
        return set1, set2

    diffset = []
    for element in set_1:
        if element not in set_2:
            diffset.append(element)
    for element in set_2:
        if element not in set_1:
            diffset.append(element)
    return diffset
