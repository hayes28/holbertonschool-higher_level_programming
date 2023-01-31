#!/usr/bin/python3
"""Creating a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
