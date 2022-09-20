#!/usr/bin/python3
def uppercase(str):
    """this test for the case of an alphabet"""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
