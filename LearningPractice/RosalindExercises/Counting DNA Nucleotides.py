

# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s
#  of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

# nt means nucleotides

s = "ATGCTTCAGAAAGGTCTTACG"

count_A = s.count('A')
count_C = s.count('C')
count_G = s.count('G')
count_T = s.count('T')

print(f"A: {count_A}")
print(f"C: {count_C}")
print(f"G: {count_G}")
print(f"T: {count_T}")
