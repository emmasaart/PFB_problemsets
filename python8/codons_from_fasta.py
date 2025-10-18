#!/usr/bin/env python3

import sys
#take user input fasta file
fasta = sys.argv[1]

#build dictionary of fasta gene-seq pairs from user input
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

#iterature through each sequence and break into codons
import re
codons_stored = {}
for gene_id in fasta_data:
    codon_list = []
    for codon in re.findall(r'(.{3})', fasta_data[gene_id]):
        codon_list.append(codon)
    codons_stored[gene_id] = codon_list

with open ('Python_08.codons-frame-1.nt','w') as fasta_write:
    for gene in codons_stored:
        fasta_write.write(f'{gene}\n')
        fasta_write.write(f'{codons_stored[gene]}\n')

#reverse complement each sequence
fwd_and_back = {}
for gene_id in fasta_data:
    rev = fasta_data[gene_id].replace('A','t').replace("T","a").replace("G","c").replace("C","g")
    rev = rev.upper()
    rev = rev[::-1]
    fwd_and_back[gene_id] = [fasta_data[gene_id],rev]

#get all six reading frames and print to a new file
more_codons_stored = {}
with open ('Python_08.codons-6frames.nt','w') as fasta_write:
    for gene_id in fwd_and_back:
        fasta_write.write(f'{gene_id}\n')
        codon_list = []
        for seq in fwd_and_back[gene_id]:
            for start in range(3):
                codon = re.findall(r'.{,3}',seq[start:])
                codon_list.append(codon)
            more_codons_stored[gene_id] = codon_list
        fasta_write.write(f'{more_codons_stored[gene_id]}\n')
