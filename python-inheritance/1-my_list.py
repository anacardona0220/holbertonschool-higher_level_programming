#!/usr/bin/python3
'''Write a class MyList that inherits from list'''


class MyList(list):
    '''prints the list, but sorted'''

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
