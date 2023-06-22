#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints it to stdout.

    Arguments:
    - filename (str): The name of the file to read (optional). If not provided,
      an empty string is assumed.

    No file permission or file existence exceptions are handled, as the 'with'
    statement is used.

    Usage:
    - read_file()                 # Reads a file without specifying the name
    - read_file('file.txt')       # Reads the 'file.txt' file

    """

    with open(filename, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea.rstrip())
