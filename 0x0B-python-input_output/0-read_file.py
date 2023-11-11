#!/usr/bin/python3
"""define text reading function"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end"")
