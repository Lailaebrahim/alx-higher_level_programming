#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    try:
        for i in range(list_length):
            try:
                if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                    if my_list_2[i] != 0:
                        my_list.append(my_list_1[i] / my_list_2[i])
                    else:
                        print("division by 0")
                        my_list.append(0)
                else:
                    print("wrong type")
                    my_list.append(0)
            except IndexError:
                print("out of range")
    except ZeroDivisionError:
        print("division by 0")
    finally:
        print(my_list)
        return my_list
