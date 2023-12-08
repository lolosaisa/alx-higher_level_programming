#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, expect q and e"""

for letter in range(97, 123):
    if letter in {113, 101}:
        continue
    print("{}".format(chr(letter)), end="")
