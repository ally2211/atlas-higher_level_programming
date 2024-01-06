#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = 0
    prev_value = 0

    for element in reversed(roman_string):
        value = roman_numerals[element]
        if value < prev_value:
            roman_number -= value
        else:
            roman_number += value
        prev_value = value

    return roman_number
