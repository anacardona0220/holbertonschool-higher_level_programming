#!/usr/bin/python3
"""a class MyList that inherits """


class MyList(list):
    """
    Prints the list in sorted order (ascending sort).
    Returns:
    list: newList ascending sort
    """

    def __init__(self, *args, **kwargs):
        if args and args[0] is None:
            raise TypeError("'None' object is not iterable")
        super().__init__(*args, **kwargs)

    def append(self, item):
        if item is None:
            raise TypeError("'None' object is not iterable")
        super().append(item)

    def print_sorted(self):
        newList = sorted(self)
        print(newList)
