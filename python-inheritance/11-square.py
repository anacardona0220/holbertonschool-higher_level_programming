#!/usr/bin/python3

"""
Square class that inherits from the Rectangle class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.

    Attributes:
        size (int): The size of the square (equal width and height).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        """
        return f"[Square] {self.__size}/{self.__size}"
