#!/usr/bin/python3
""" Reads text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ Reads and prints to stdout """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
