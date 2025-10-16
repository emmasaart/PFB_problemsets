#!/usr/bin/env python3

num_lines = 0 
id_line = 0 
chars = 0
nts = 0
seq_lines = 0

with open ("Python_06.fastq", "r") as file_read:
    for line in file_read:
        line = line.rstrip()
        num_lines += 1 #lines counter
        chars += len(line) #total character counter
        if num_lines % 2 == 0: #for lines 2&4 (repeating), which are of the same length
            nts += len(line) #number nts is characters in that line
            seq_lines += 1 #count number of sequence lines
print(f'''total num_lines:{num_lines}
total seq IDs: {num_lines/4}
total characters: {chars}
total nucleotides: {nts/2}
average line length: {chars/num_lines}
average sequence length: {nts/seq_lines}\n''')
#divide nt by 2 because there are also an equal number of quality chars in that count