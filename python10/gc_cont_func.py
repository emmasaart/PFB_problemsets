#!/usr/bin/env python3

def gc_content(seq):
    c_count = seq.count('C')
    g_count = seq.count('G')
    seq_len = len(seq)
    gc_cont = (c_count + g_count)/seq_len
    return(gc_cont)

dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
percGC = gc_content(dna)
print(f'GC content of sequence is {percGC:.2%}')