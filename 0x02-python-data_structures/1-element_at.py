#!/usr/bin/python3
def element_at(my_list, idx):
    return None if idx < 0 or idx not in range(len(my_list)) else my_list[idx]
    # The function will return the element at a specific index in the list,
    # if the index is valid, otherwise it will return None.
