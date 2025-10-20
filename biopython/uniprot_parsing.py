#!/usr/bin/env python3

import Bio
from Bio import SeqIO
import argparse
import re

parser = argparse.ArgumentParser(
    description=("This script is a blast parser")
)

#add arguments
parser.add_argument("file", help="path to input fasta filename")
parser.add_argument("species", help="species to count sequences present")
args = parser.parse_args()

#arguments appear in args
filename = args.file
species_count = args.species

#get number of sequences
sequence_count = 0
for seq_record in SeqIO.parse(filename, "fasta"):
    sequence_count += 1

#make a list of the IDs
id_list = []
for seq_record in SeqIO.parse(filename, "fasta"):
    id_list.append(seq_record.id)

#make a list of the descriptions
desc_list = []
for seq_record in SeqIO.parse(filename, "fasta"):
    for found in re.finditer(r'.+=(\w+\s\w+).+GN=.+',seq_record.description):
        desc = found.group(1)
        desc_list.append(desc)

count_species = 0
for species in desc_list:
    if species == species_count:
        count_species += 1

#write a file containing all sequences for species Salmonella paratyphi B
with open ("s_paratyphi.prot.fa","w") as file_write:
    for seq_record in SeqIO.parse(filename, "fasta"):
        for found in re.finditer(r'.+=(Salmonella paratyphi B).+',seq_record.description):
            file_write.write(f'>{seq_record.id}{seq_record.description}\n{seq_record.seq}\n')