#!/usr/bin/env python3

import re

id = []
seq = []
with open ("Python_07.fasta","r") as fasta_read:
    current_seq=''
    for line in fasta_read:
        line = line.rstrip()
        if line.startswith('>'):
            for found in re.finditer(r'^>(\S+)',line):
                id.append(found.group(1))
            if current_seq != "":
                seq.append(current_seq)
                current_seq = ''
        else:
            current_seq=current_seq+line
seq.append(current_seq)
fasta_dict = dict(zip(id,seq))
print(fasta_dict)

