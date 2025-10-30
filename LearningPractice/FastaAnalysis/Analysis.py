
#cds:Coding DNA Sequence

#GQ487580 | GQ487581 | GQ487582 | GQ487583 | GQ487584 | GQ487585 |
#GQ487586 | GQ487587 | GQ487588 | GQ487589 | GQ487590 | GQ487591 |
#GQ487592 | GQ487593 | GQ487594 | GQ487595 | GQ487596


#gen ZP3: encodes zona pellucida glycoprotein 3 (ZP3), 
# a protein that is a crucial structural component of the zona pellucida, 
# the extracellular matrix surrounding eggs and early embryos. 
# It plays a vital role in fertilization by acting as the primary sperm receptor, 
# initiating sperm binding.

#Transiciones vs transversiones: Cambios entre nucleotides. 

#*********************
#Stop Codons
#*********************
#UAA

#UAG

#UGA

#*********************

#TAA

#TAG

#TGA

#*********************

#>70 Grupo monofiletico
#<70 Es posible que estos no forman grupo monofiletico

from Bio import AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline
from pathlib import Path
import os

# Get the folder where this script is located
script_dir = Path(os.path.dirname(__file__))

# Input and output files in the same folder
fasta_path = script_dir / "sequence.fasta"
aligned_path = script_dir / "aligned.fasta"

# Run Clustal Omega
clustalomega_cline = ClustalOmegaCommandline(
    infile=str(fasta_path),
    outfile=str(aligned_path),
    verbose=True,
    auto=True,
    force=True
)
stdout, stderr = clustalomega_cline()

print("Alignment saved to:", aligned_path)

# Read and display alignment
alignment = AlignIO.read(str(aligned_path), "fasta")
print(alignment)
