from Bio.Seq import Seq

# Nível 1: Contagem de bases
sequencia = "ATGCGTACGTAGCTAG"
print(f"Tamanho: {len(sequencia)} | Gs: {sequencia.count('G')}")