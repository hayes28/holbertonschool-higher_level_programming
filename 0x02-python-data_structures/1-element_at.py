#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx not in range(len(my_list)):
        return None
    return my_list[idx]
