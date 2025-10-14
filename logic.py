#!/usr/bin/env python3

my_number = 50

if my_number == 50:
    print("Aye Captain")
else:
    print("Not true")


if my_number > 0:
    print(f"{my_number} is positive")
    if my_number < 50:
        if my_number % 2 == 0:
            print(f"{my_number} is even and less than 50")
        elif my_number % 2 == 1:
            print(f"{my_number} is less than 50 and odd")
    elif my_number > 50:
        if my_number % 3 == 0:
            print(f"{my_number} is greater than 50 and divisible by 3")
        else:
            print(f"{my_number} is larger than 50 and indivisible by 3")
    elif my_number == 50:
        print (f"{my_number} is equal to 50")
elif my_number < 0:
    print(f"{my_number} is negative")
elif my_number == 0:
    print(f"{my_number} equals zero")

