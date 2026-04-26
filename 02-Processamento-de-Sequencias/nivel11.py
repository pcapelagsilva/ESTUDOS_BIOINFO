# ABRINDO A CAIXA DE FERRAMENTAS
from Bio import SeqIO

caminho = "ESTUDOS_BIOINFO/paciente_nivel11.fasta"

caminho_saida = caminho.replace('paciente_nivel11.fasta', 'gene_ativo_nivel11.txt')

# FAZENDO A LEITURA DO ARQUIVO EM FASTA
for registro in SeqIO.parse(caminho, 'fasta'):
    dna = registro.seq # SEQUENCIA DE DNA COMPLETA
    dna_inicio = dna.find('ATG') # POSIÇÃO DO CÓDON DE START

    if dna_inicio != -1: # SE ENCONTRAR (DIFERENTE DE -1), FAZ O CORTE

        gene_ativo = registro.seq[dna_inicio:] # CORTA O GENE DO ATG ATÉ O FINAL

        print(F"Achamos o códon de start!, O DNA se inicia na casa {dna_inicio}")

        with open(caminho_saida, "w") as f_saida: # SALVANDO O ARQUIVO
            f_saida.write("-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=\n")
            f_saida.write(f"ID do Gene: {registro.id}\n")
            f_saida.write("------------------------------------\n")
            f_saida.write(f"Sequencia iniciando no códon de start: {gene_ativo}\n")
            f_saida.write("-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=\n")
    else:
        print("Nenhum Start Codon (ATG) encontrado.")
        print("\n =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(f'O ARQUIVO ESTA PRONTO E SALVO EM: {caminho_saida}')
