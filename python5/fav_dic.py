#!/usr/bin/env python3

#make a list o favorite things
favorites = {'book':'jitterbug perfume','song':'i wont back down','tree':'cedar'}
#print favorite book using a variable
fav_book = 'book'
print(favorites[fav_book])
print(favorites['tree'])
print('\n')

#add favorite organism to dictionary
fav_org = 'cat'
favorites['organism']=fav_org
#print favorite organism sing fav_thing variable
fav_thing = 'organism'
print(favorites[fav_thing])
print('\n')

#use a for loop to print each key and value
for thing in favorites:
    print(thing, favorites[thing])
print('\n')

#use command line entry to print a favorite thing
import sys

thing = sys.argv[1]
print(favorites[thing])
print('\n')

#print all keys to the user
for thing in favorites:
    print(f'key:{thing}')
print('\n')

#change the value of favorite organism
favorites['organism'] = 'dog'
print(favorites['organism'])
print('\n')

#change fav_thing to be input in the command line
fav_thing = sys.argv[2]
print(favorites[fav_thing])
