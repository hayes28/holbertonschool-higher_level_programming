#!/usr/bin/python
def multiply_by_2(a_dictionary):
    # It creates a copy of the original dictionary called 'new'
    # It iterates over the keys of the 'new' dictionary
    new = a_dictionary.copy()
    for i in new:
        # and multiplies the value of each key by 2
        new[i] = new[i] * 2
        # It returns the modified 'new' dictionary
    return new
