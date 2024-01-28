#!/usr/bin/python3
"""
Module Doc: Rectangle Class
"""


def read_file(filename=""):
    """
    Function Doc: read a file
    """
    with open(filename, "r", encoding="utf-8") as f:
        # Check if the file is empty
        if os.path.getsize(filename) == 0:
            print("File is empty.")
        else:
            for line in f:
                print(line, end='')
