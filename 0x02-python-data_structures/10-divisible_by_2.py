#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        if x % 2 == 0:
            # For each item, it
            # checks if the item is divisible by 2
            # using the modulus operator %
            new_list.append(True)
            # If the item is divisible by 2,
            # it appends True to the new_list
        else:
            new_list.append(False)
            # If the item is not divisible by 2,
            # it appends False to the new_list
    return new_list
    # The function will return a new list
    # containing the Boolean values indicating
    # whether each element in the original list
    # is divisible by 2 or not.
