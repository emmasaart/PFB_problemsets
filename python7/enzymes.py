#!/usr/bin/env python3

import re
#build a dictionary from the file containing enzyme paired with recognition pattern
enz_dict = {}
count = 0
with open ("bionet.txt", "r") as file_read:
    for line in file_read:
        line = line.rstrip()
        count += 1 
        if count <= 10:
            continue
        else:
            for element in re.finditer(r'(\S+.\S+)\s{2,}(\S+)',line):
                enz = element.group(1)
                seq = element.group(2)
                enz_dict[enz] = seq

#take command line argument for name of enzyme file and fasta file with a sequence to be cut
import sys
fasta = sys.argv[1]

sequence = ''

#read in sequence from use input fasta
with open (fasta,'r') as fasta_read:
    for line in fasta_read:
        if line[0] == '>':
            continue
        else:
            sequence += line

#remove new lines
sequence = sequence.replace('\n','')

#user input enzyme
enz_in = sys.argv[2]

for key in enz_dict:
    if key == enz_in:
        cut_site = enz_dict[key]

#alter cut site to ensure ^ presence
for nts in cut_site:
    if '^' in cut_site:
        continue
    else:
        cut_site = '^'+cut_site+'^' 

#create a cut site version without ^
cut_for_seq = cut_site.replace('^','')

#insert cut sites into sequence:
for site in re.finditer(cut_for_seq,sequence):
    seq_new = re.sub(cut_for_seq,cut_site,sequence)

#cut fragments
seq_split = seq_new.split('^')

#sort split sequences
sorted_split = sorted(seq_split, key=len, reverse=True)
print(sorted_split)
