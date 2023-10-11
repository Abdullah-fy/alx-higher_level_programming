#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary_keys = sorted(a_dictionary)
    for key in sorted_dictionary_keys:
        print(f"{key}: {a_dictionary[key]}")
