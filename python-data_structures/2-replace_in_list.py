#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    lenlist = len(my_list)
    if (idx >= 0):
        if idx < lenlist:
            my_list[idx] = element
            return(my_list)
        else:
            return(my_list)
    else:
        return(my_list)
