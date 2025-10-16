#!/usr/bin/env python3

#open file and read each line
header = []
all_seqs = []
with open ("Python_06.fasta","r") as fasta_read:
    current_seq=''
    for line in fasta_read:
        line = line.rstrip()
        if line[0] == '>':
            line = line.replace('>','')
            header.append(line)
            if current_seq != "":
                all_seqs.append(current_seq)
                current_seq = ''
        else:
            current_seq=current_seq+line
all_seqs.append(current_seq)
fasta_dict = dict(zip(header,all_seqs))

print(fasta_dict)