#!/usr/bin/env python3
import re

#find every occurrence of nobody and print the position
line_num = 0
with open ("Python_07_nobody.txt", "r") as poem_read:
    for line in poem_read:
        line_num += 1
        for found in re.finditer(r'(Nobody)',line):
            position = found.start(1)
            print(f'found on line {line_num}, position {position+1}')

#go through the file and replace 'Nobody' with 'Emma'
with open ("Python_07_nobody.txt", "r") as poem_read, open ("Emma.txt", "w") as poem_write:
    for line in poem_read:
        poem_write.write(re.sub(r'Nobody','Emma',line))