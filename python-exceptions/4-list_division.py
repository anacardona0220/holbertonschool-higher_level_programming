#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resultList = []
    for item in range(list_length):
        try:
            operacion = (my_list_1[item] / my_list_2[item])

        except TypeError:
            operacion = 0
            print("wrong type")

        except ZeroDivisionError:
            operacion = 0
            print("division by 0")

        except IndexError:
            operacion = 0
            print("out of range")

        finally:
            resultList.append(operacion)

    return resultList
