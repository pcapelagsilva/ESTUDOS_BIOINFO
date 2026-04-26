from Bio import SeqIO

caminho = 'ESTUDOS_BIOINFO/meu_dna_nivel9.fasta'

for registro in SeqIO.parse(caminho, 'fasta'):
    trecho = registro.seq[6:21]

    caminho_saida = caminho.replace('meu_dna_nivel9.fasta', 'dna_limpo_nivel9.txt')

    with open(caminho_saida, 'w') as f_saida:
        f_saida.write(f'ID do gene: {registro.id}\n')
        f_saida.write(f'Trecho da sequencia: {trecho}\n')
    print(f'O Arquivo pronto - sem as 5 primeiras e últimas sequências - salvo em {caminho_saida}')
