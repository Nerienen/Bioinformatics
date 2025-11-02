# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, you may return any one of them.)

from pathlib import Path
from collections import defaultdict

# Get the path to the script's directory
script_dir = Path(__file__).parent

# Build the full path to the file inside the 'Data' folder
fasta_file = script_dir / "Data" / "fasta_9.txt"

def read_fasta(filename):
    """Reads a FASTA file and returns a list of sequences."""
    sequences = []
    with open(filename) as f:
        seq = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ''
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

def consensus_and_profile(sequences):
    """Computes consensus string and profile matrix from a list of DNA sequences."""
    n = len(sequences[0])
    profile = {'A':[0]*n, 'C':[0]*n, 'G':[0]*n, 'T':[0]*n}
    
    # Fill profile matrix
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1
    
    # Build consensus string
    consensus = ''
    for i in range(n):
        max_nuc = max('ACGT', key=lambda nuc: profile[nuc][i])
        consensus += max_nuc
    
    return consensus, profile

# Read file and compute results
sequences = read_fasta(fasta_file)
consensus, profile = consensus_and_profile(sequences)

print(consensus)
for nuc in 'ACGT':
    print(f"{nuc}: {' '.join(map(str, profile[nuc]))}")
