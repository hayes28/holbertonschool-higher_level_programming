#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord('c'): ""})
    new_string = my_string.translate({ord('C'): ""})
    return new_string    
