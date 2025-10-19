#!/usr/bin/env python3
import re
import argparse

#parse command line arguments using arg parser
parser = argparse.ArgumentParser(
    description = ('This program takes a FASTA file and max line length'
                   'as arguments and outputs reformatted sequence' 
                   'to specified max line length in FASTA format') 
)

parser.add_argument("file", help = 'path to input fasta file name')
parser.add_argument("max_length", type=int, help = "number of nt per line")
parser.add_argument("--outfile", help="optional: supply output fie name", dest="out")
args= parser.parse_args()

#arguments to appear in args
filename = args.file
max_length = args.max_length
if args.out:
    print('writing output to', args.out)


#make a function that takes dna sequene as input and formats it so line is no longer than 60 nts long
def seq_format(dna):
    new_seq = ''
    lines = re.findall(r'.{,60}',dna)
    for line in lines:
        new_seq += (f'{line}\n')
    return(new_seq)

#modify that function so it will work for sequences with new lines
def seq_format_nl(dna):
    dna = dna.replace('\n','')
    new_seq = ''
    lines = re.findall(r'.{,60}',dna)
    for line in lines:
        line.replace('\n','')
        new_seq += (f'{line}\n')
    return(new_seq)  

#modify function so it takes DNA string and max length
def seq_format_spec(dna,length):
    dna = dna.replace('\n','')
    new_seq = ''
    lines = re.findall(rf'.{{,{length}}}',dna)
    for line in lines:
        line.replace('\n','')
        new_seq += (f'{line}\n')
    return(new_seq) 

dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG0CTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''
formatted_seq = seq_format_spec(dna,80)

#fasta reader function
def fasta_reader(fasta):
    fasta_data = {}
    gene_id = ''
    seq_build = ''
    with open (fasta, 'r') as fasta_read:
        for line in fasta_read:
            line=line.rstrip()
            if re.search(r'^>',line):
                gene_id = line
                seq_build = ''
            else:
                seq_build += line
            fasta_data[gene_id] = seq_build
    return fasta_data

#reformatter function for generated fasta dictionary
def fasta_formatter(fasta_dict):
    for gene_id in fasta_dict:
        sequence = fasta_dict[gene_id]
        print(f'{gene_id}')
        formatted_seq = seq_format_spec(sequence,max_length)
        print(formatted_seq)

fasta_dict = fasta_reader(filename)
fasta_formatter(fasta_dict)

