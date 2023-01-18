#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
            return

    length = len(roman_string)
    romstr = roman_string
    number = 0
    numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
    for i in range(length):
        if i + 1 < length and numbers[romstr[i]] < numbers[romstr[i + 1]]:
            number -= numbers[romstr[i]]
        else:
            number += numbers[romstr[i]]
        return number
    return (0)
