#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_2 = my_list[:]
    for i in my_list:
        if i % 2 == 0:
            div_2[i] = True
        else:
            div_2[i] = False
    return div_2
