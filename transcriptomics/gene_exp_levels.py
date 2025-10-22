#!/usr/bin/env python

import sys, re

filename = sys.argv[1]

gene_id_dict = {}
with open (filename, 'r') as file_read:
    for line in file_read:
        line = line.rstrip()
        temp_split = line.split('\t')
        if gene_id := re.search(r'^[^\^]+', temp_split[2]).group(0):
            if gene_id not in gene_id_dict:
                gene_id_dict[gene_id] = set()
        gene_id_dict[gene_id].add(temp_split[0])


gene_reads_count = {}
for gene_id in gene_id_dict:
    reads_count = len(gene_id_dict[gene_id])
    print(gene_id)
    print(gene_id_dict[gene_id])
    gene_reads_count[gene_id] = reads_count

gene_reads_count = dict(sorted(gene_reads_count.items(), key =lambda reads_tuple: reads_tuple[1], reverse = True))

for gene_id in gene_reads_count:
    print(f'{gene_id}:\t{gene_reads_count[gene_id]}')
        


        