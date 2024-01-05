#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    lenlist = len(my_list)
    new_list = my_list.copy()
    if (idx >= 0):
        if idx < lenlist:
            new_list[idx] = element
            return (new_list)
        else:
            return (my_list)
    else:
        return (my_list)
