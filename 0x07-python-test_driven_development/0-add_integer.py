#!/usr/bin/python3
""" This module is for a function that add_integer."""

def add_integer(a, b=98):
    """Adds two values of type integer.

    Args:
        a: the first integer.
        b: default 98, the second integer

    Raises:
       TypeError: if a, b are not int or float.


    Returns:
       The sum of two integers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
