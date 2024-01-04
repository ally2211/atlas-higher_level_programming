#!/usr/bin/python3

def uppercase(input_str):
    result_str = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_ascii = ord(char) - ord('a') + ord('A')
            result_str += "{}".format(chr(uppercase_ascii))
        else:
            result_str += char
    print(result_str)
