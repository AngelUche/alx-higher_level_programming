#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass

    my_list.reverse()
    for numbers in range(len(my_list)):
        print("{:}".format(my_list[numbers]))