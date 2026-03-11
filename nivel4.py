from Bio.SeqUtils import gc_fraction

seq = "ATGCGCTAGCTAGCTAG"
gc = gc_fraction(seq) * 100
print(f"Conteúdo GC: {gc:.2f}%")