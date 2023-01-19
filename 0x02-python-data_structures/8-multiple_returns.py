#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if sentence else None)
    # The function returns a tuple with the length of the
    # sentence and the first character of the sentence if
    # the sentence is not empty, otherwise it will return None.
