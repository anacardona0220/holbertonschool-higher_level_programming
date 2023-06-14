#!/usr/bin/python3
''' create  empty class'''


class Square:

    '''definition class square'''

    def __init__(self, size=0):
        ''' Private instance attribute:size
        Args:
            param1 (size): Description of `param1`.'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
