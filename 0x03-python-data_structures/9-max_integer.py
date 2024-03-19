#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        maxN = my_list[0]
        for i in range(len(my_list)):
            if maxN < my_list[i]:
                maxN = my_list[i]
        return maxN
