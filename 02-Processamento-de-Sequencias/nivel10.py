#📊 Nível 10: Comparador de Variantes
#Vamos simular a comparação entre dois pacientes.

#Tarefa: Crie dois arquivos: paciente_A.fasta e paciente_B.fasta. Coloque sequências quase iguais, mas mude uma ou duas letras.

#O "Pulo do Gato": O Python deve ler os dois e imprimir no terminal: "As sequências são iguais?" (Use o operador ==). Além disso, calcule o Conteúdo GC de cada um para ver qual é mais estável.

#Saída: Um print comparativo no terminal.

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

caminho_1 = 'ESTUDOS_BIOINFO/paciente_A_nivel10.fasta'
caminho_2 = 'ESTUDOS_BIOINFO/paciente_B_nivel10.fasta'

for registro1 in SeqIO.parse(caminho_1, 'fasta'):
    seq_1 = registro1.seq

for registro2 in SeqIO.parse(caminho_2, 'fasta'):
    seq_2 = registro2.seq

print('As sequências são iguais?')
print('-=-=-=-='*10)
if seq_1 == seq_2:
    print('SIM, as duas sequencias são iguais!')
else:
    print('NÃO, duas sequencias são diferentes!')  
print('As sequências são: ')
print(f'\n Paciente A: {seq_1}')
print(f'\n Paciente B: {seq_2}')
