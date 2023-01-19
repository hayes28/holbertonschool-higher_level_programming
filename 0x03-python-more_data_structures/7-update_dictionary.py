#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # This function takes in a dictionary, a key and a value as parameters
    # It updates the value of the key in the dictionary
    # If the key is not in the dictionary, it adds the key-value pair to
    # the dictionary
    a_dictionary[key] = value
    # It returns the updated dictionary
    return a_dictionary
