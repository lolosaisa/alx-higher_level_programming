#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = abs(number) % 10
if number < 0:
    dig = -dig
    print("Last digit of {} is {} and is ".format(number, dig), end = "")
    if dig > 5:
        print("and is greater than 5")
    elif dig == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
