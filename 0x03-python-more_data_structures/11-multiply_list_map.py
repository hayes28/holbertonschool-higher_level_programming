#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Uses built-in 'map' function to apply the 'lambda' function
    # to each element of the list
    # 'lambda' multiplies each element of the list by the number parameter
    # Converts the map object to a list, returns modified list
    return list(map((lambda x: x * number), my_list))
