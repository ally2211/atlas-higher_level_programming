#!/usr/bin/python3


def uniq_add(my_list=[]):
    if my_list is None:
        return my_list

    hold = []
    sumelement = 0
    for element in my_list:
        if element not in hold:
            sumelement += element
            hold.append(element)
    return sumelement
