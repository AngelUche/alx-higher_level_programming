#!/usr/bin/python3
def max_integer(my_list=[]):

    max_num = my_list[0]
    if my_list == " ":
        return None
    for number in my_list:
        if number > max_num:
            max_num = number
    return max_num
