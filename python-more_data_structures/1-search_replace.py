#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None or search < 0 or search > len(my_list) + 1:
        return my_list

    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
