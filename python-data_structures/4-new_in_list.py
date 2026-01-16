#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list
    if idx < 0:
        return list
    if idx > len(my_list):
        return list
    my_list[idx] = element
    return my_list
