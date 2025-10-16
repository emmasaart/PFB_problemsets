#!/usr/bin/env python3

#iterate over sequence and count each unique nt in a dictionary
gene_id = []
seq = []
nt_counts = {}
with open ("Python_06.seq.txt","r") as seq_read:
    for line in seq_read:
        line = line.rstrip()
        gene_id,seq = line.split('\t')
        seq_set = set(seq)
        for nt in seq_set:
            count = seq.count(nt)
            nt_counts[nt] = count
        total_nt = len(seq)
        gc_cont = ((int(nt_counts['G'])+int(nt_counts['C']))/total_nt)
        print(f'GC content of {gene_id}:{gc_cont:.2%}')
print(f'counts: {nt_counts}')



    
    
    
    
    