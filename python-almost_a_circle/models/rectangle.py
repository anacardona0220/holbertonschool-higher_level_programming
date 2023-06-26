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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
