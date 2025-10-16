#!/usr/bin/env python3

#create a list of dna sequences
dna = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#create a for loop printing sequence lenth and sequence separated by a tab
for nt in dna:
    print (f"{len(nt)}\t{nt}")
print('\n')
#print position in list of each sequence
for nt in dna:
    print(f"{dna.index(nt)}\t{len(nt)}\t{nt}")
print('\n')
#sort DNA by fragment size and print
dna_length = sorted(dna, key = len, reverse = True)
for nt in dna_length:
    print(nt)