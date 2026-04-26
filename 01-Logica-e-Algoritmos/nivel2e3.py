from Bio.Seq import Seq

# Nível 2 e 3: Tradução (DNA -> Proteína)
meu_dna = Seq("ATGCGTACGTAG")
proteina = meu_dna.translate()
print(f"Proteína: {proteina}")
