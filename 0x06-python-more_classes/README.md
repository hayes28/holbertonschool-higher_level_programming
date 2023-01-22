# README for project 0x06- python-more_classes

## Tasks
0. Real definition of a rectangle
Write a class Rectangle that defines a rectangle by:
* Private instance attribute: width:
    + property def width(self): to retrieve it
    + property setter def width(self, value): to set it:
    - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    + property def height(self): to retrieve it
    + property setter def height(self, value): to set it:
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* You are not allowed to import any module

1. Area and Perimeter
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
* Private instance attribute: width:
    + property def width(self): to retrieve it
    + property setter def width(self, value): to set it:
    - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    + property def height(self): to retrieve it
    + property setter def height(self, value): to set it:
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* You are not allowed to import any module

1. Area and Perimeter
Write a class Square that defines a square by: (based on square.py)
* Private instance attribute: width:
    + property def width(self): to retrieve it
    + property setter def width(self, value): to set it:
    - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: length:
    + property def length(self): to retrieve it
    + property setter def length(self, value): to set it:
    - length must be an integer, otherwise raise a TypeError exception with the message length must be an integer
    - length must be an integer, otherwise raise a TypeError exception with the message length must be an integer
* Private instance attribute: area:
    + property def area(self): to retrieve it
    + property setter def area(self, value): to set it:
    - area must be an integer, otherwise raise a TypeError exception with the message area must be an integer
    - area must be an integer, otherwise raise a TypeError exception with the message area must be an integer
* Private instance attribute: perimeter:
    + property def perimeter(self): to retrieve it
    + property setter def height(self, value): to set it:
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
    + if width or height is equal to 0, perimeter is equal to 0
* You are not allowed to import any module

2. String representation
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
* Private instance attribute: width:
    + property def width(self): to retrieve it
    + property setter def width(self, value): to set it:
    - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    - if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
    + property def height(self): to retrieve it
    + property setter def height(self, value): to set it:
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
    + if width or height is equal to 0, perimeter is equal to 0
* print() and str() should print the rectangle with the character #: (see example below)
    + print() should print a string that defines a rectangle by: (based on 1-rectangle.py)
    + if width or height is equal to 0, return an empty string
* You are not allowed to import any module

3. Eval is magic
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
* Private instance attribute: width:
    + property def width(self): to retrieve it
    + property setter def width(self, value): to set it:
    - width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    - if width is less than 0, raise a ValueError exception with the message width must be >= 0
    + property def height(self): to retrieve it
    + property setter def height(self, value): to set it:
    - height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    - if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area:
    + if width or height is equal to 0, area is equal to 0
* Public instance method: def perimeter(self): that returns the rectangle perimeter:
    + if width or height is equal to 0, perimeter is equal to 0
* print() and str() should print the rectangle with the character #: (see example below)
    + if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
* You are not allowed to import any module
