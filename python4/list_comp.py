#!/usr/bin/env python3

#make a list using list comprehension with every number between 0 and 99
comp = [x for x in range(100)]

#make a list using list comprehension with every number between 1 and 100
comp2 = [1 +x for x in range(100)]

#print every number including min and max using sys.argv and print only odd
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])

for num in range(min,max+1):
    if num %2 == 1:
        print(num)

