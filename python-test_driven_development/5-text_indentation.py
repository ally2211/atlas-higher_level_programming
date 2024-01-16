#!/usr/bin/python3
def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?', and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True
    for char in text:
        if new_line and char == ' ':
            continue
        else:
            print(char, end='')
            new_line = False

        if char in '.?:':
            print("\n\n", end='')
            new_line = True
