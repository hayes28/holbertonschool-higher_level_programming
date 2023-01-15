#!/usr/bin/python3
def uniq_add(my_list=[]):
    # This function takes in a list and returns
    # the sum 'i' of unique elements in the list.
    i = 0
    # Using set to remove duplicates and convert it back to list
    result = list(set(my_list))
    # iterating through the elements in the list
    for j in result:
        i += j
    return i
