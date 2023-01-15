#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # It checks if the key is in the dictionary
    # If the key is in the dictionary, it deletes
    # the key-value pair using the del statement
    if key in a_dictionary:
        del a_dictionary[key]
        # It returns the updated dictionary
    return a_dictionary
