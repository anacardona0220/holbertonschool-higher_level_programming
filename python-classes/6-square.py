#!/usr/bin/python3
"""Creating the square class whit Private instance attribute: size"""


class Square:
    """Square class definition and Instantiation with optional siza and
    optional position"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """allows to get the value of size and returns self.__size"""

    @property
    def size(self):
        return self.__size

    """allows assigning a value to size and performs type and
    value validation"""

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """allows to get the value of size and returns self.__position"""

    @property
    def position(self):
        return self.__position

    """position must be a tuple of 2 positive integers, otherwise
    raise a TypeError"""

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Public instance method that returns the current square area"""

    def area(self):
        return self.__size * self.__size

    """Public instance method that prints in stdout the square
    with the character #:"""

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
