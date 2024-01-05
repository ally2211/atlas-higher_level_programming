#!/usr/bin/python3


def element_at(my_list, idx):
    lenlist = len(my_list)
    if (idx >= 0):
        if idx < lenlist:
            return(my_list[idx])
        else:
            return("None")
    else:
        return("None")
