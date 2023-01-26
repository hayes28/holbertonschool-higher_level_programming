#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Testing first for valid input to the function,
    then printing some of the inputted text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    text_period = text.replace(". ", ".\n\n")
    text_question = text_period.replace("? ", "?\n\n")
    text_colon = text_question.replace(": ", ":\n\n")

    print(text_colon, end="")
