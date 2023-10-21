#!/usr/bin/python3
from sys import argv
__name__ == "__main__"
if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("1 argument:")
    print(f"1: {argv[1]}")
else:
    print(f"{len(argv) - 1} arguments:")
    for x in range(1, len(argv)):
        print(f"{x}: {argv[x]}")
