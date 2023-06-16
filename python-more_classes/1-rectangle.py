#!/usr/bin/python3
'''class Rectangle that defines a rectangle'''


class Rectangle:
    '''This class contain constructor and methods'''
    def __init__(self, width=0, height=0):
        '''Constructor'''
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''The width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height of the rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
