#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        # The function checks if the
        # index is less than 0 or greater than
        # or equal to the length of the list
        return my_list
        # If the check is True, the function
        # returns the original list without
        # making any changes
    del(my_list[idx])
    # If the check is False, it deletes the
    # element at the given index using the
    # del() function
    return my_list
    # The function will delete an element
    # at a specific index in the list, if
    # the index is valid, otherwise it will
    # return the original list without making
    # any changes.
