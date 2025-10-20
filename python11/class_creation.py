#!/usr/bin/env python3

class DNARecord(object):
    def __init__ (self,sequence,gene_name,organism):
        self.sequence = sequence.upper()
        self.gene_name = gene_name
        self.organism = organism
    def seq_length(self):
        length = len(self.sequence)
        return length
    def nt_comp(self):
        nt_count = {}
        unique = set(self.sequence)
        for nt in unique:
            count = self.sequence.count(nt)
            nt_count[nt] = count
        return nt_count
    def gc_cont(self):
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        seq_len = len(self.sequence)
        gc_cont = (c_count + g_count)/seq_len
        return(gc_cont)
    def fasta_formatter(self):
        print(f'>{self.gene_name}\n{self.sequence}')
    def make_list(self):
        
    def seq_compare(self):


dna_rec_obj_1 = DNARecord('ATTCCCGGGG','ABC1','Drosophila melanogaster')
print(f'name:{dna_rec_obj_1.gene_name} sequence:{dna_rec_obj_1.sequence} organism:{dna_rec_obj_1.organism}')

sequence_len = dna_rec_obj_1.seq_length()
print(f'sequence length: {sequence_len}')

nuc_cont = dna_rec_obj_1.nt_comp()
print(f'nucleotide content:{nuc_cont}')

gc_cont = dna_rec_obj_1.gc_cont()
print(f'GC content: {gc_cont:.2%}')

dna_rec_obj_1.fasta_formatter()
