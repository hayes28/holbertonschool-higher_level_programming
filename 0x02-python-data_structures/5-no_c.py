#!/usr/bin/python3
def no_c(my_string):
    return my_string.translate({ord(x): None for x in 'cC'})
