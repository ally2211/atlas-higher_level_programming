#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if not my_list:  # Check if the list is empty
        return None

    if 0 <= idx < len(my_list):
        my_list.pop(idx)

    return my_list
