#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indexcount = 0
    try:
        while indexcount is not x:
            print(my_list[indexcount], end="")
            indexcount +=1
    except IndexError:
        pass
        print()
        return indexcount
