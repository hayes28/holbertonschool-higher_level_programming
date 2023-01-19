#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx not in range(len(my_list)):
        # The function checks if the index is less than 0
        # or not in the range of the length of the list
        return None
    return my_list[idx]
    # The function will return the element at a specific index in the list,
    # if the index is valid, otherwise it will return None.
