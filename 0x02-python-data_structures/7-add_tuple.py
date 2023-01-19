#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    # The function assigns the first element
    # of tuple_a to variable a1, if the length
    # of tuple_a is greater than 0, otherwise assigns 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    # The function assigns the second element of
    # tuple_a to variable a2, if the length of
    # tuple_a is greater than 1, otherwise assigns 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1+b1, a2+b2)
    # The function will add the values of the
    # two tuples element by element and return
    # a tuple with the sum of the elements.
