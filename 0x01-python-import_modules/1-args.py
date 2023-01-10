#!/usr/bin/python3
import sys

if __name__ == '__main__':
    
    if (len(sys.argv) - 1) == 0:
        print("0 arguments.")
    else:
        if (len(sys.arg) - 1) == 1:
            print((len(sys.argv) -1), "argument:")
        else:
            print((len(sys.argv) - 1), "argument:")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
