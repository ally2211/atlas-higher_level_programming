#!/usr/bin/python3
"""
Module Doc: Rectangle Class
"""


def read_file(filename=""):
    """
    Function Doc: read a file
    """
    with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line, end='')

