#!/usr/bin/env python3

gene_id = ()
seq = ()
with open("Python_06.seq.txt","r") as seq_read:
    for line in seq_read:
        line = line.rstrip()
        gene_id,seq = line.split('\t')
        seq = seq.replace('A','t').replace("T","a").replace("G","c").replace("C","g")
        seq = seq.upper()
        seq = seq[::-1]
        print(f">{gene_id} reverse complement \t{seq}\n")

