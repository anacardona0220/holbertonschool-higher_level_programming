#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_score = None
    best_key = None
    found = False

    for key, value in a_dictionary.items():
        if not found or value > best_score:
            best_score = value
            best_key = key
            found = True
    return best_key
