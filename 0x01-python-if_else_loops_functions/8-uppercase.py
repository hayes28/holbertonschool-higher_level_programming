#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = chr(ord(c) - 32) if ord(c) >= ord('a') and ord(c) <= ord('z') else c
        print("{:s}".format(char), end="")
    print('')
