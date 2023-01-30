#!/usr/bin/python3
""" 
Author: Heather Hayes 
Date: Jan, 2023
class MyList that inherits from list
"""


class MyList(list):
    """ Inherits from list """
    
    def __inti__(self):
        """ initializes MyList sub class, brings all attributes from list """
        
        super().__init__()
        
    def print_sorted(self):
        """ Prints sorted list (ascending) """
        
        print(sorted(self))
