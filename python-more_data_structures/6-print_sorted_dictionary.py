#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return 1

    sorted_keys = sorted(a_dictionary)
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = a_dictionary[key]

    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
