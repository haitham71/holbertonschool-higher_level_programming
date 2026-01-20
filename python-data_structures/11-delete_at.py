#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list[idx] < 0 or my_list[idx] >= 5 :
        return my_list
    del my_list[idx] 
    new_list = my_list
    return new_list
