#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10
if number < 0:
    dig = -dig
    print("Last digit of {} is {} and is ".format(number, dig), end = "")
elif number > 0:
    dig = +dig
    print("Last digit of {} is {} and is ".format(number, dig), end = "")
    if dig > 5:
        print("greater than 5")
    elif dig == 0:
        print("0")
    else:
        print("and is less than 6 and not 0")
