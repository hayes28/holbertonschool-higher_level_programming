#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    This function takes in a string as an argument and
    converts it to a Roman numeral.
    """
    # check if input is not a string or is empty
    if type(roman_string) != str or not roman_string:
        return 0

    # Initialize variables to store the final integer
    # value and the previous value
    count = 0
    last = 0

    # Create a dictionary of Roman numerals and
    # their corresponding integer values
    romNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}

    # Iterate through the input string
    for x in roman_string:

        # check if the last value is less than the current value
        if last != 0 and last < romNum[x]:
            count -= last
        else:
            count += last
        last = romNum[x]
        # add the last value
    count += last
    return count
