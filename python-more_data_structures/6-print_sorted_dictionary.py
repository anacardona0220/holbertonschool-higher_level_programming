#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.keys())
    for key in sorted_dictionary:
        print("{}: {}".format(key, a_dictionary[key]))
