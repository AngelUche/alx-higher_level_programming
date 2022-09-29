#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    return [var if var != search else replace for var in my_list]
