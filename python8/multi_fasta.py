#!/usr/bin/env python3

import sys

#take user input fasta file
fasta = sys.argv[1]

#calculate nt composition for each sequence using a data structure
fasta_data = {}
gene_id = ''
seq_build = ''
with open (fasta, 'r') as fasta_read:
    for line in fasta_read:
        line=line.rstrip()
        if line[0]=='>':
            gene_id = line
            seq_build = ''
        else:
            seq_build += line
        fasta_data[gene_id] = seq_build

counts_fasta = {}
for gene_id in fasta_data:
    unique_nts = set(fasta_data[gene_id])
    sequence = fasta_data[gene_id]
    counts_fasta[gene_id] = {}
    for nt in unique_nts:
        count = sequence.count(nt)
        counts_fasta[gene_id][nt]=count
print(counts_fasta)
