#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return

    max_score = None
    max_key = None
    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_key = key
            max_score = value
    return max_key
