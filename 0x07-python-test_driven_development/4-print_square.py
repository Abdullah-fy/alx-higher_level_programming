#!/usr/bin/python3
"""print a square with character #"""


def print_square(size):
    """function to print square
    Args:
    size (int) is the size length of the square
    Raises:
    TypeError if size not int
    ValueErrror if size < 0"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
