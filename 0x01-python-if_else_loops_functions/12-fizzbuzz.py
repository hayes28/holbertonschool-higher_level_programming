#!/usr/bin/python3
def fizzbuzz():
     """
    Prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
    For numbers which are multiples of both three and five print “FizzBuzz”
    """
for number in range(1, 101): # Iterate through the numbers 1 to 100
     if number % 3 == 0 and number % 5 == 0: # check if the number is divisible by 3 and 5
          print('FizzBuzz ', end='') # if yes, print FizzBuzz
     elif number % 3 == 0:  # check if the number is divisible by 3
         print('Fizz ', end='') # if yes, print Fizz
     elif number % 5 == 0: # check if the number is divisible by 5
         print('Buzz ', end='') # if yes, print Buzz
     else:
          print(f'{number} ', end='')
