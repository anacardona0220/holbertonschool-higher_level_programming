#!/usr/bin/python3
''' create  empty class'''


class Square:

    '''definition class square'''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        '''returns the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''  to set it
        Args:
            param1 (value): Description of `param1`.'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''returns the area of the square'''
        return self.__size ** 2
