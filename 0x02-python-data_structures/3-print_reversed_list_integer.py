#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for x in reversed(my_list):
            # The function uses a for loop to iterate over each
            # item in the list in reverse order using the reversed() function.
            print("{:d}".format(x))
