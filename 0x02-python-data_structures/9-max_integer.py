#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort()
    # If the list is
    # not empty, it sorts the list
    # using the sort() method, which sorts
    # the elements of the list in ascending order.
    return my_list[-1]
    # The function will return the largest
    # integer in the list, if the list is not empty
    # otherwise it will return None.
