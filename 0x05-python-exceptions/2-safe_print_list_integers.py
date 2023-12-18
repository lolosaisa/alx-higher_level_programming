#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    #variable i and c are used to iterate throught the list snd store cout respectively
    i, c = 0, 0
    while i < x:
        try:
            print("{:d}".format(i))
            c +=1
        except (TypeError, ValueError):
            pass
        print()
        return c
