#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        # The function checks if the index is less than 0 or greater than
        # or equal to the length of the list
        return my_list
    else:
        my_list[idx] = element
        return my_list
        # The function will replace an element at a specific index in the list,
        # if the index is valid, otherwise it will return
        # the original list without making any changes.
