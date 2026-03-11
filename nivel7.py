from Bio import SeqIO

# Importante: O caminho deve estar idêntico ao nome da sua pasta
caminho = "ESTUDOS_BIOINFO/meu_dna_nivel7e8.fasta"

for registro in SeqIO.parse(caminho, "fasta"):
    print(f"ID: {registro.id}")
    print(f"DNA: {registro.seq}")