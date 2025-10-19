#!/usr/bin/env python3

def rev_comp(seq):
    rev_comp = seq.replace('A','t').replace("T","a").replace("G","c").replace("C","g")
    rev_comp = seq.upper()
    rev_comp = seq[::-1]
    return rev_comp

reverse_comp = rev_comp('ACGTT')
print(reverse_comp)