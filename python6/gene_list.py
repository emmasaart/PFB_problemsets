#!/usr/bin/env python3

#read in tf genes
tf_genes = set()
with open("ferret_transcriptionFactors.tsv.txt","r") as tf_read:
    for line in tf_read:
        line= line.rstrip()
        tf_genes.add(line)

#read in stem cell genes
sc_genes = set()
with open("ferret_stemcellproliferation_genes.tsv.txt","r") as sc_read:
    for line in sc_read:
        line= line.rstrip()
        sc_genes.add(line)

#read in pigmentation genes
pig_genes = set()
with open("ferret_pigmentation_genes.tsv.txt","r") as pig_read:
    for line in pig_read:
        line= line.rstrip()
        pig_genes.add(line)

sc_and_pig = pig_genes & sc_genes
tf_and_sc = sc_genes & tf_genes
tf_and_pig = pig_genes & tf_genes

#print overlaps
print(f''' overlapping stem cell proliferation and pigmentation genes: {len(sc_and_pig)}
overlapping stem cell proliferation genes and transcription factors: {len(tf_and_sc)}
overlapping pigmentation genes and transcription factors: {len(tf_and_pig)}''')