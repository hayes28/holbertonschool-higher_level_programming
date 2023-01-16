#!/usr/bin/python3
def best_score(a_dictionary):
    # It checks if the dictionary is not empty
    if a_dictionary:
        # If not empty the max function is used with the key arg
        # set to a lambda function, which returns the key of max value
        return max(a_dictionary, key=lambda x: a_dictionary[x])
