#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Using set to remove duplicates and convert it back to list
    result = list(set(my_list))
    return sum(result)
