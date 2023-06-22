#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''


def write_file(filename="", text=""):
    """
    write a UTF-8 encoded text file and prints it to stdout.

    Arguments:
    - filename (str): The name of the file to read (optional). If not provided,
      an empty string is assumed.

    No file permission or file existence exceptions are handled, as the 'with'
    statement is used.
    """

    with open(filename, "w", encoding="utf-8") as archivo:
        num_char = archivo.write(text)
        return num_char
