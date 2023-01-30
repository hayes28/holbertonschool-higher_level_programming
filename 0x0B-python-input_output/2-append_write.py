#!/usr/bin/python3
""" ppends a string at the end of a text file (UTF8)
returns the number of characters added """


def append_write(filename="", text=""):
    """ Reads and prints to stdout """
    with open(filename, "a", encoding="utf-8") as my_file:
        return(my_file.write(text))
