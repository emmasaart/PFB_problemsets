#!/usr/bin/env python3

#problem set python 2
#question 1: assign value to a variable and confirm value
my_number = 50

if my_number == 50:
    print("Aye Captain")
else:
    print("Not true")

#question 3: if/else positive or negative
if my_number > 0:
    print(f"{my_number} is positive")
    if my_number < 50: #question 5: is value positive and > or < 50?
        if my_number % 2 == 0: #question 6: is value <50 and even?
            print(f"{my_number} is even and less than 50")
        elif my_number % 2 == 1:
            print(f"{my_number} is less than 50 and odd")
    elif my_number > 50: 
        if my_number % 3 == 0: #question 7: is value >50 and divisible by 3?
            print(f"{my_number} is greater than 50 and divisible by 3")
        else:
            print(f"{my_number} is larger than 50 and indivisible by 3")
    elif my_number == 50:
        print (f"{my_number} is equal to 50")
elif my_number < 0: #question four: for if value = zero
    print(f"{my_number} is negative")
elif my_number == 0:
    print(f"{my_number} equals zero")

