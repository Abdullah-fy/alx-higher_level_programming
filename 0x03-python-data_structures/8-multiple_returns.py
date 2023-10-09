#!/usr/bin/python3
def multiple_returns(sentence):
    my_List = []
    length = len(sentence)
    if (length == 0):
        a = None
    else:
        a = sentence[0]
    my_List.append(length)
    my_List.append(a)
    return (tuple(my_List))
