#!/usr/bin/python3
'''Write the first class rectangle'''
from models.base import Base


class Rectangle(Base):
    """
    Clase Rectangle que hereda de la clase Base.

    Representa un rectángulo con ancho, altura, posición x e y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor de la clase Rectangle.

        Args:
            width (int): Ancho del rectángulo.
            height (int): Altura del rectángulo.
            x(int, optional): Posición x del rectángulo.
            y(int, optional): Posición y del rectángulo.
            id (int, optional): ID opcional para asignar al rectángulo.
        Attributes:
            width (int): Ancho del rectángulo.
            height (int): Altura del rectángulo.
            x (int): Posición x del rectángulo.
            y (int): Posición y del rectángulo.
            id (int): ID del rectángulo.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        '''calculate to area of rectangle'''
        return self.__width * self.__height

    def display(self):
        """Imprime en stdout la representación visual del rectángulo."""
        for _ in range(self.height):
            print("#" * self.width)
