#!/usr/bin/python3
def uppercase(string):
    for a in string:
        value = ord(a)
        if value >= 97 and value <= 122:
            value = value - 32
        print("{:c}".format(value), end="")
    print("")
