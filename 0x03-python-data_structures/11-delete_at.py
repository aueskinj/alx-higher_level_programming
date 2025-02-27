#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) -1:
        return my_list
    else:
        new_list = my_list[:idx] + my_list[idx+1:]  # Create a new list excluding index n
        my_list[:] = new_list  # Modify the original list in-place
    return new_list
