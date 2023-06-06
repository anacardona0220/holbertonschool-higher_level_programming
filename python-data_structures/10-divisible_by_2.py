#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    else:
        div_2 = []
        for i in my_list:
            if i % 2 == 0:
                div_2.append(True)
            else:
                div_2.append(False)
        return div_2

# #!/usr/bin/python3
# def divisible_by_2(my_list=[]):
#     return [num % 2 == 0 for num in my_list]