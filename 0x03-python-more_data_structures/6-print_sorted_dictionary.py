#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # It prints the key-value pairs of the dictionary in a sorted order
    # Using list comprehension and the sorted() function to sort the keys
    # then it prints the key-value pairs using the format() method
    [print(f"{i}: {a_dictionary[i]}") for i in sorted(a_dictionary)]
