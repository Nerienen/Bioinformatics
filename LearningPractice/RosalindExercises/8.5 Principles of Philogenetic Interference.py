from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor, ParsimonyScorer
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import matplotlib.pyplot as plt

# --- Input sequences (aligned) ---
sequences = {
    "Cow":   "ATGAAAGTAAGGGAGTATTCTCCTAAGGACAAGAGAAATGCCTCCTTCC TAAATA",
    "Deer":  "ATGAAAGTAAGGGAGTATTCTCCTAAGGACAAGAGAAATGCCTCCTTCC TAAATA",
    "Whale": "ATGAAAGTAAGGGAGTATTCTCCTAAGGACAAGGGAAATGCCTCCTTCC TAAATC",
    "Hippo": "ATGAAAGTAAGGGAGTATTCTCCTAAGGACAAGGGAAATGCCTCCTTCC TAAATC",
    "Pig":   "ATGAAAGTAAGGGAGTATTCTCCTAAGGACAAGGGAAATGCCTCCTTCC TAAATC",
    "Camel": "ATGAAAGTAAGGGAGTATTCTCCTAAGGACAAGGGAAATGCCTCCTTCC TAAATC"
}

# Clean sequences
seqs = {name: seq.replace(" ", "") for name, seq in sequences.items()}

# Define offset and sites of interest
offset = 140
positions = [151, 162, 166, 177, 194]

# Build Multiple Sequence Alignment
records = [SeqRecord(Seq(seq), id=name) for name, seq in seqs.items()]
alignment = MultipleSeqAlignment(records)

# --- Build a simple Neighbor-Joining tree ---
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)
constructor = DistanceTreeConstructor()
nj_tree = constructor.nj(dm)

print("Full NJ Tree:")
Phylo.draw_ascii(nj_tree)

# --- Parsimony scoring for each position ---
scorer = ParsimonyScorer()
for pos in positions:
    index = pos - offset - 1
    site_records = [
        SeqRecord(Seq(seqs[name][index]), id=name)
        for name in seqs
    ]
    site_alignment = MultipleSeqAlignment(site_records)

    score = scorer.get_score(nj_tree, site_alignment)
    print(f"\nPosition {pos} parsimony score: {score}")

# --- Optional: visualize tree with matplotlib ---
Phylo.draw(nj_tree)
plt.show()
