#!/usr/bin/python3

for ltr in range(97, 123):
    if chr(ltr) not in ['q', 'e']:
        print(f"{chr(ltr)}", end="")
