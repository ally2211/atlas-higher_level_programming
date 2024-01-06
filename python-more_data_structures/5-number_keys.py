#!/usr/bin/python3

def number_keys(a_dictionary):
    if a_dictionary is None:
        return 0

    numberofkeys = 0
    for element in a_dictionary:
        numberofkeys += 1

    return numberofkeys
