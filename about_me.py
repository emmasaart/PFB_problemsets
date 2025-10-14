#!/usr/bin/env python3

name = "Emma"
print(f"My name: {name}")

color = "Purple"
print(f"My favorite color:{color}")

activity = "Running"
print("My favorite activity:",activity)

animal = "Penguin"
print("My favortie animal:",animal)

import sys

name2 = sys.argv[1]
color2 = sys.argv[2]
activity2 = sys.argv[3]
animal2 = sys.argv[4]

print('my name is '+ name2+ ' and my favorite color is '+ color2+ '. i like '+ activity2+ ' and '+ animal2+".")