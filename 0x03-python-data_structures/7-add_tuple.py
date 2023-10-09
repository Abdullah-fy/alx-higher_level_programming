#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tu3 = []
    for i in range(2):
        if i >= len(tuple_a):
            value1 = 0
        else:
            value1 = tuple_a[i]
        if i >= len(tuple_b):
            value2 = 0
        else:
            value2 = tuple_b[i]
        tu3.append(value1 + value2)
    return tuple(tu3)
