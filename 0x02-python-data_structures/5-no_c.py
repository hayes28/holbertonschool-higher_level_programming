#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(x): None for x in 'cC'})
    # translate() method takes a dictionary as an argument where
    # keys are the characters to be replaced and values are their replacement.
    return new_string
