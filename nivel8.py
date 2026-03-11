from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Cole aqui o que você copiou do "Copy Relative Path"
caminho = "ESTUDOS_BIOINFO/meu_dna_nivel7e8.fasta" 

for registro in SeqIO.parse(caminho, "fasta"):
    # Processamento
    trecho = registro.seq[0:90]
    gc = gc_fraction(trecho) * 100
    proteina = trecho.translate()

    # Para salvar, use o mesmo caminho, trocando apenas o final do nome do arquivo
    caminho_saida = caminho.replace("meu_dna_nivel7e8.fasta", "relatorio_final_nivel8.txt")
    
    with open(caminho_saida, "w") as f_saida:
        f_saida.write(f"ID: {registro.id}\n")
        f_saida.write(f"GC: {gc:.2f}%\n")
        f_saida.write(f"Proteina: {proteina}\n")

print(f"✅ Arquivo salvo com sucesso em: {caminho_saida}")