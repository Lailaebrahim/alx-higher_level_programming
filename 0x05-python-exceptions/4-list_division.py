#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    try:
        for i in range(list_length):
            if isinstance(my_list_1[i], int) and isinstance(my_list_2[i], int):
                my_list.append(my_list_1[i] / my_list_2[i])x
    except TypeError:
        print("wrong type")
        ret = 0
    except IndexError:
        print("out of range")
        ret = 0
    except ZeroDivisionError:
        print("division by 0")
        ret = 0
    finally:
        print(my_list)
    return my_list
