#!/usr/bin/env python3

import Bio
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(
    description=("This script is a fasta parser")
)

#add arguments
parser.add_argument("file", help="path to input fasta filename")

args = parser.parse_args()

#arguments appear in args
filename = args.file

#make GC content function
def gc_content(seq):
    c_count = seq.count('C')
    g_count = seq.count('G')
    seq_len = len(seq)
    gc_cont = (c_count + g_count)/seq_len
    return(gc_cont)

#get sequence name, description, and sequence
# for seq_record in SeqIO.parse(filename,"fasta"):
#     print('ID', seq_record.id)
#     print('Description', seq_record.description)
#     print('Sequence', seq_record.seq)


#get stats about the total content present
sequence_count = 0
total_nt = 0
length_dict = {}
gc_content_dict = {}
for seq_record in SeqIO.parse(filename, "fasta"):
    sequence_count += 1
    total_nt += (len(seq_record.seq))
    length_dict[seq_record.id] = len(seq_record.seq)
    percent_gc = gc_content(seq_record.seq)
    gc_content_dict[seq_record.id] = percent_gc


min_length = min(length_dict.values())
max_length = max(length_dict.values())
min_GC_cont = min(gc_content_dict.values())
max_GC_cont = max(gc_content_dict.values())
averge_gc_content = (sum(gc_content_dict.values())/len(gc_content_dict))

print(f'''total number of sequences:{sequence_count}
total number of nucleotides: {total_nt}
average length of sequences: {total_nt/sequence_count}
shortest sequence length: {min_length}
longest sequence length: {max_length}
avg GC content: {averge_gc_content}
lowest GC content: {min_GC_cont}
highest GC content: {max_GC_cont}''')
    
