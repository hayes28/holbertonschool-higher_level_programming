#!/usr/bin/python3
import random # import the random module to generate random number
number = random.randint(-10, 10) # generate a random integer between -10 and 10
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print("0 is zero") # if the number is equal to 0, it is zero
else:
    print(f"{number} is negative")
