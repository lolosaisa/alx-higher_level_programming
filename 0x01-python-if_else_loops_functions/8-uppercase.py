#!/usr/bin/python3

def uppercase(str):
    """prints string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{:s}".format(c), end="")
            print()
