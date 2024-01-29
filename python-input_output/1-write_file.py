#!/usr/bin/python3
"""
Module Doc: write doc
"""


def write_file(filename="", text=""):
    """
    Function Doc: write text to a file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\n")
