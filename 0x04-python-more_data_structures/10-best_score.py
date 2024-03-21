#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        return keys[values.index(max(values))]
