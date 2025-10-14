#!/usr/bin/env python3

import sys

value = int(sys.argv[1])

if value > 0:
    print(f"{value} is positive")
    if value < 50:
        if value % 2 == 0:
            print(f"{value} is even and less than 50")
        elif value % 2 == 1:
            print(f"{value} is less than 50 and odd")
    elif value > 50:
        if value % 3 == 0:
            print(f"{value} is greater than 50 and divisible by 3")
        else:
            print(f"{value} is larger than 50 and indivisible by 3")
    elif value == 50:
        print (f"{value} is equal to 50")
elif value < 0:
    print(f"{value} is negative")
elif value == 0:
    print(f"{value} is equal to zero")