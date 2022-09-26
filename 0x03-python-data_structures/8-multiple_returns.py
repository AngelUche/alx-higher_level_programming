#!/usr/bin/python3

def multiple_returns(sentence):
    new_tuple = ()
    len_tuple = 0
    for letters in sentence:
        if sentence[0] == '':
            sentence[0] = None
        len_tuple += 1

    else:
        new_tuple = sentence[0]
    return len_tuple, new_tuple
