#motif: same interval in genome of two organisms that might have the same function
#repeats: intervals that repeat sveral times in dna, they likely serve a purpose just like similar words in a human language do
#Alu repeat: repeat of ~300 pairs in human genome that occurs ~1 000 000 times ~300bp long, hasn't been found to be benefitial  
#bp: combi of two bonded complementary pairs
#position in a string = total number of symbols to it's left, including itself (U in AGU = 3)

s = "TCCTAGGTCCTAGGTCCTAGGTCCTAGGTCCTAGGACTCCTAGGTCCTAGGACGGCTCCTAGGTCCTAGGCTCCTAGGCTATCCTAGGCTCCTAGGCGTTGCGCTACTCCTAGGTCCTAGGTGTCCTAGGCTCCTAGGTCCTAGGTCCTAGGTCCTAGGTCCTAGGCCTTTGATCCTAGGCGCATCCTAGGTCTCCTAGGTCTAGCTAGAGTTCCTCCTAGGTCCTAGGTTCCTAGGTCCTAGGTCCTAGGAGTCGTGTATCCTAGGTCCTAGGTTATCCTAGGAGGTCCTAGGCTTCCTAGGTCCTAGGCTCCTAGGTCCTAGGCGTCCTAGGTCCTAGGTCCTAGGCTCCTAGGAAACTGGCTCCTAGGCCTCCTAGGATTCCTAGGAGTCCTAGGAGTCCTAGGACTTGTCCTAGGGTTCCTAGGTCCTAGGGCCTCCTAGGACAGCCTTCCTAGGTCCTAGGATCCTAGGGTCCTAGGGCACGTCCTAGGGAGGTCCTAGGTATCCTAGGTCCTAGGTCCTAGGGTCCTAGGTTATGACTCTCCTAGGTTCCTAGGTCCTAGGTCCTAGGCTTTTACTGATTCCTAGGGAGAGTTCCTAGGGATGCCTCCTAGGGTCTTCCTAGGTCCTAGGCGAGGTAGTCCTAGGGTCCTAGGCCGGTTCCTAGGATTAAACCTGTCCTAGGTTGCTTCCTAGGTATTGTCTCAGGCCCGGTCCTAGGCCTTCCTAGGTTCCTAGGTGGCGCAGCCAATCCTAGGTTCCTAGGCATTCCTAGGCTCCTAGGTCCTAGGGTAATTCCTAGGTCCTAGG"
t = "TCCTAGGTC"

def find_substring_locations(s, t):
    #Initializes an empty list called positions where we will store the starting positions of t in s
    positions = []

    #Loops over all possible starting indices in s where t could fit.

#len(s) - len(t) + 1 ensures we don’t go past the end of s.

#For example, if s has length 10 and t has length 3, the loop goes from i = 0 to i = 7 (inclusive).
    
    for i in range(len(s) - len(t) + 1):
        #slices the string from index i to i + len(t) - 1
        if s[i:i+len(t)] == t:
            #If the substring matches, add the 1-indexed position to the positions list.
            positions.append(i + 1)  # +1 for 1-indexed position

            #returns the list of starting positions where t appears in s
    return positions



# Get positions
positions = find_substring_locations(s, t)

# Print output in the required format
print(" ".join(map(str, positions)))
