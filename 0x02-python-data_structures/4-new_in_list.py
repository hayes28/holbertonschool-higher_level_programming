#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx not in range(len(my_list)): 
    # If the index is out of range, it will return my_list.
        return my_list
    else: 
    # Otherwise, it will make a copy of my_list
    # and replace the value in that position with element.
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
