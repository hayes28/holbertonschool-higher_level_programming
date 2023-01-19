#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # This function takes in a list, a search item, and a replacement item
    # It then replaces all instances of the search item
    # with the replacement item in the list
    # and returns the modified list
    return [replace if item == search else item for item in my_list]
# my_list = inital list
# search = element to replace in list
# replace = new element
