#!/usr/bin/env python3

import re
#read fasta file in and find header
header_list = []
with open ("Python_07.fasta", "r") as fasta_read:
    for line in fasta_read:
        header_list += re.findall(r'^>.+',line)

#if line is a header, extract id
with open ("Python_07.fasta", "r") as fasta_read:
    for line in fasta_read:
        for found in re.finditer(r'^>(\S+)\s(.+)',line):
            print(f'id: {found.group(1)} desc: {found.group(2)}')