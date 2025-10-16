#!/usr/bin/env python3
import random

sequence = 'ATGTGTA'
seq_list = list(sequence)
#create a for loop for N times (length of sequence)
for N in seq_list:
    A = random.randrange(len(sequence))
    B = random.randrange(len(sequence))
    seq_list[A],seq_list[B]=seq_list[B],seq_list[A]
print(''.join(seq_list))