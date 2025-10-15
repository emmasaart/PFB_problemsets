#!/usr/bin/env python3

#define loop
my_loop = [101,2,15,22,95,33,2,27,72,15,52]
my_loop.sort()
sum_even = 0
sum_odd = 0

#print only even values
for num in my_loop:
    if num %2 == 0:
        print(num)
        sum_even = num + sum_even
    if num %2 == 1:
        print(num)
        sum_odd = num + sum_odd
print(f'''the sum of the even numbers is {sum_even}
the sum of the odd numbers is {sum_odd}''')
