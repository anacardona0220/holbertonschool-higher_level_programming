#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return new_list
 # c_element = set()
    # for i in set_1:
    #     if i in set_2:
    #         c_element.add(i)
    # return c_element    

    # c_element = set(filter(lambda x: x in set_1, set_2))
    # return c_element  