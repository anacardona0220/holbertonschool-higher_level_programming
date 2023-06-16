#!/usr/bin/python3
'''function that prints a text with 2 new lines after each of these characters: ., ?'''


def text_indentation(text):
    '''prints a text'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for caracters in ".:?":
        text = (caracters + "\n\n").join(
            [line.strip(" ") for line in text.split(caracters)])

    print("{}".format(text), end="")
