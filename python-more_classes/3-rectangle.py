#!/usr/bin/python3
"""
This module define a Rectangle based in the
previous module
"""


class Rectangle:
    """
    This class contain constructor and methods
    """

    def __init__(self, width=0, height=0):
        """
        The method constructor:
        Parameters:
        width: the purpose is set the value
        height: the purpose is set the value
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter parameters: itself"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter parameters: value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter parameters: itself"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter parameters: value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):

        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rectangle += '#' * self.__width + '\n'
        return rectangle.rstrip('\n')
