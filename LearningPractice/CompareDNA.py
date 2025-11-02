



sequences = {
    "Cow":      "GTGCC",
    "Deer":     "GTGCC",
    "Whale":    "GTCTC",
    "Hippo":    "GTCTC",
    "Pig":      "GCGTC",
    "Peccary":  "CCGTC",
    "Camel":    "ACACT",
    "Outgroup": "ACTCT"
}




# difference counting
def differenceCounting(a, b):
    difference = 0

    #zip (a, b) places to compare a letter from "a" with the letter from "b" in the same position

    for x, y in zip(a, b):
        if x != y:
            difference += 1
    return difference

names = list(sequences.keys())





# table print

print("       ", end="")
for n in names:
    print(f"{n:12}", end="")
print()


for n1 in names:
    print(f"{n1:8}", end=" ")
    for n2 in names:
        d = differenceCounting(sequences[n1], sequences[n2])
        print(f"{d:<12}", end="")
    print()