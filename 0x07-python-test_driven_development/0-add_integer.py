#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """ function to add two integer.
    Args:
    a : first int
    b : sec int
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
