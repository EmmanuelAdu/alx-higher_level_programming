#!/usr/bin/python3
'''This function divides elements by elements 2 lists'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
