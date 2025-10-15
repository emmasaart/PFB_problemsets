#!/usr/bin/env python3

#create a string and print it and its type
taxa_string = 'sapiens : erectus : neanderthalensis'
print(taxa_string)
print(type(taxa_string))

#split the string into a list
taxa_list = taxa_string.split(" : ")
print(taxa_list)
#print index #1
print(taxa_list[1])
#print type to confirm list 
print(type(taxa_list))
#sort the list alphabetically
sorted_taxa_alpha = sorted(taxa_list)
print(sorted_taxa_alpha)
#sort the list by length of string
sorted_taxa_len = sorted(taxa_list, key=len)
print(sorted_taxa_len)