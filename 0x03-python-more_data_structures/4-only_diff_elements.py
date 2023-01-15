#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # This function takes two sets as parameters
    # and returns one set without duplicates

    # Using the symmetric_difference() method '^' to combine elements
    # from set_1 and set_2
    return set_1 ^ set_2
