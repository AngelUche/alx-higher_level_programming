#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 or set_2 is None:
        return set_1.symmetric_difference(set_2)
