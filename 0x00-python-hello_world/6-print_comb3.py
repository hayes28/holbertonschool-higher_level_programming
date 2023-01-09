#!/usr/bin/python3
for j in range(10):
    for e in range(j + 1, 10):
        if (j == 8 and e == 9):
            print("{:d}{:d}".format(j, e))
        else:
            print("{:d}{:d}".format(j, e), end=', ')
