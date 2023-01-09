#!/usr/bin/python3

for letters in range(ord('a'), ord('z')+1):
    letters = chr(letters)
    if letters not in "qe":
        print(letters, end="")
