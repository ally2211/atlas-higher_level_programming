#!/usr/bin/python3
"""
Module Doc: write doc
"""


def append_write(filename="", text=""):
    """
    Function Doc: Append text to a file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")
