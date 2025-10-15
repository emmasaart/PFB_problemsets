#!/usr/bin/env python3

#use a while loop to print 1-100
count=0
sum=0
while count <101:
    print(f"count={count}")
    sum = sum + count #ad in a running sum of each number
    count+=1
print(f"sum is equal to {sum}") #outside the while loop, print the sum

#use a while loop to calculate factorial of 10
count=1
factorial = 1
while count <= 10:
    factorial = factorial * count
    count+=1
print(f"factorial of 10 is {factorial}")
