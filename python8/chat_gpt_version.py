#!/usr/bin/env python3

def read_fasta(filename):
    """Read a multi-FASTA file and return a dictionary of {header: sequence}."""
    sequences = {}
    header = None
    seq_chunks = []

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                # Save previous sequence if any
                if header:
                    sequences[header] = "".join(seq_chunks)
                header = line[1:]  # remove '>'
                seq_chunks = []
            else:
                seq_chunks.append(line.upper())
        # Don't forget the last sequence
        if header:
            sequences[header] = "".join(seq_chunks)

    return sequences


def split_into_codons(sequence):
    """Split a DNA sequence into codons (triplets) in the first reading frame."""
    codons = [sequence[i:i+3] for i in range(0, len(sequence) - len(sequence) % 3, 3)]
    return codons


def main():
    fasta_file = input("Enter the path to the multi-FASTA file: ").strip()
    sequences = read_fasta(fasta_file)

    for header, seq in sequences.items():
        codons = split_into_codons(seq)
        print(f">{header}")
        print(" ".join(codons))


if __name__ == "__main__":
    main()
