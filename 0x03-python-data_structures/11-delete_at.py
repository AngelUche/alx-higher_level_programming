#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx < 0 and idx > len_list:
        return my_list
    del my_list[idx]
    return my_lis
