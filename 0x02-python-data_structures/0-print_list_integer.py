#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
    # The function uses a for loop to iterate over each item in the list.
        print("{:d}".format(x)) 
    # The item is passed to the format() method of the string "{:d}",
    #  which is a placeholder for an integer.

    # The format() method replaces the placeholder with the item from the list,
    # and then the string is passed to the print() function to be output to the console.
