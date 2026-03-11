# RELEMBRANDO PYTHON - como usar o print com letras
#print("Olá mundo, meu nome é Pedro e estou relembrando como utilizar o Python!!!!")

# RELEMBRANDO PYTHON - como usar o print com números
#print(7,4)
#print(7+4)

# RELEMBRANDO PYTHON - como o usar input para fazer perguntas
#input('Qual seu nome? ')
#input('Qual a sua idade? ')
#input('Qual seu peso? ')

# RELEMBRANDO PYTHON - como o usar int (números inteiros)
#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro:'))
#s = n1 + n2
#print('A soma vale', s)

# RELEMBRANDO PYTHON - como o usar .format (sempre deve ser feita com chaves = {})
#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro:'))
#s = n1 + n2
#print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# RELEMBRANDO PYTHON - como o usar float (O valor sempre será dado com vírgula - número real)
#n = float(input('Digite um valor: '))
#print(n)

# RELEMBRANDO PYTHON - como o usar bool (valor lógico ou booleanos "verdadeiro ou falso" - o resultado sempre será dado como True ou False)
#n=bool(input('Digite um valor: '))
#print(n)

#Outra forma de se utilizar o True or False (verdadeiro ou falso) é através dos atalhos '.is...', que podem variar de diversas formas
#n=input('Digite uma letra: ')
#print(n.isalpha())
#print(n.isnumeric())
#print(n.isdecimal())
#print(n.istitle())
#print(n.isupper())
#print(n.isalnum())

# RELEMBRANDO PYTHON - como o usar operadores aritiméticos: + (soma), - (subtração), * (multiplicação), / (divisão), ** (potencia), // (raiz) e % (porcentagem). A ordem de precedência desses operadores são: 
# 1°Parentesês () 
# 2° Potencias ** 
# 3° Multiplicação, Divisão, Raiz, Porcentagem (*, /, //, %)
# 4° Adição e Subtração (+ e -)
# n1 = int(input('Um valor: '))
# n2 = int(input('Outro valor: '))
# sm= n1+n2
# sb=n1-n2
# d=n1/n2
# m=n1*n2
# p=n1**n2
# r=n1//n2
# pc=n1%n2
# print('A soma vale {}'.format(n1+n2))
# print('A subtração vale {}'.format(n1-n2)),
# print('A divisão vale {}'.format(n1/n2))
# print('A multiplicação vale {}'.format(n1*n2))
# print('A potencia vale {}'.format(n1**n2))
# print('A raiz vale {}'.format(n1//n2))
# print('A porcentagem vale {}'.format(n1%n2))
#print('O resultado de todas as operações aritiméticas são: soma {}, subtração {}, divisão {}, multiplicação {}, potencia {}, raiz {} e porcentagem {}.'.format(sm, sb, d, m, p, r, pc))

#Também existem alguns sinais que quando postos dentro das {} do .format executam algumas ações. São eles:
#{:número} - escreve a resposta no número de espaços escolhidos
#{>} - escreve a resposta alinhada a direita
#{<} - escreve a resposta alinhada a esquerda
#{^} - escreve a resposta centralizada
#{símbolo + sinal} - completa o espaço em branco com o símbolo escolhido
#nome=input('Qual é seu nome? ')
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:=>20}!'.format(nome))
#print('Prazer em te conhecer {:=<20}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

# RELEMBRANDO PYTHON - Módulos
#O código 'import', como a própria tradução diz o que o programa deve puxar para o código, porém ele não puxa algo específico, ele puxa tudo o que esta dentro da determinda pasta
#Caso você queira algo específico da pasta, fazemos uma pequena mudança, acrescentamos o código 'from' para indicar de que pasta queremos retirar algo e logo em seguida adicionamos o 'import' especificando o que queremos utilizar.
#import math #irá importar tudo que esta na biblioteca math
#from math import ceil #ira importar apenas o 'ceil'(arrendodar) que esta dentro da biblioteca 'math'
#from math import hypot
#co = float(input('Comprimento do Cateto Oposto: '))
#ca = float(input('Comprimento do Cateto Adjacente :'))
#h = hypot(co, ca)
#print(f'O comprimento da hipotenusa desse triângulo é igual a: {h:.2f}')

# RELEMBRANDO PYTHON - Manipulando códigos
#Fatiamento = escreva o valor (o que) você deseja fatiar e logo em seguida abra '[:]', dentro você irá digitar a casa no qual você deseja que ele começe o corte e após os dois pontos a casa na qual ele deve parar o corte, se quiser que ele pule de x em x casas basta adicionar mais dois pontos e por o número de casas que você quer pular.
#frase = 'Olá bioinformata'
#trecho = frase[4:16]
#print(f'O trecho desejado da frase {frase} é {trecho}')
#Analise = serve para descobrir características do código/frase, como: tamanho, contar, achar, etc. 
#Para descobrir o tamanho do código/frase é: 'len(código/frase)';
#Para que o programa conte algo basta digitar: 'código/frase.count('o que você quer contar');
#Para o programa encontrar algo devemos digitar: 'código/frase.find('o que você quer contar');
#O operador 'in' serve para que o python verifique se determinada letra/número/palavra/etc se encontra no código/frase desejado, dando a resposta em True ou False: "'letra/número/palavra/etc'incódigo/frase"
#Para mudar algo dentro do código, como no caso da bioinformática os nucleotídeos, usamos o seguinte código: "'código/frase.replace('o que deve mudar', 'o que quero por no lugar')
#Para mudar toda a frase para letra maiuscula usamos o: 'código/frase.upper' e para minúsculo 'código/frase.lower()'
# Divisão = são códigos utilizadas para dividir strings, são eles:
#Para dividir a sua strings onde existe um espaço utilizamos o: 'código/frase.split()'
#Para juntar suas strings que estão separadas se usa o seguinte código: "".join(código/frase) - entre as aspas ("") você põe o que você usar para juntar as palavras/letras/números/etc do código/frase

# RELEMBRANDO PYTHON - Condições:
#São dividas em condições, ou seja, 'se' algo for correto faça isso 'se não' faça aquilo. No caso do Python usamos essa palavra em inglês 'if'(se) e 'else'(se não.). assim o código fica: 'if condição()': 'esle condição():'
# Por exemplo:
#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <= 3:
#    print('carro novo')
#else:
#    print('carro velho')
#print('-- FIM --')
#A gente consegue simplificar essa condição juntando tudo na mesma linha, ficando então:
#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <= 3 else 'carro velho')
#print('-- FIM --')
#Caso a estrutura se forme com condições alinhadas, ou seja, com mais de uma possibilidade a escrevemos de uma forma um pouco diferente. Ao invés de usarmos apenas os comando 'if' e 'else', entre esses dois utilizamos o código 'elif'.
#Por exemplo:
#casa = float(input('Valor da casa: R$'))
#salario = float(input("Salário do comprador: R$"))
#anos = int(input('Quantos anos de financiamento? '))
#prestação = casa / (anos * 12)
#minimo = salario *30 /100
#print('Para pagar uma casa de R${} em {} anos a prestação será de R${}'.format(casa, anos, prestação))
#if prestação <= minimo:
#    print('O empréstimo pode ser feito!')
#else:
#    print('O empréstimo será negado!')
#print('COMPARANDO: tem que pagar R${} e o mínimo é de R${}'.format(prestação, minimo))

# RELEMBRANDO PYTHON - Estrutura de repetição FOR (estrutura de laço)
# Serve para deixar o código mais inxuto, facilitando no nossa vida. Quando algo deve ser repetido ao invés de digitar o mesmo código inúmeras vezes nós podemos criar um laço de repetição (FOR) para que aquilo se repita o número de vezes que nós desejamos.
# O código deve ser escrito da seguinte forma:
# for c in range (0,10):
#   print('Oi')
#print('Fim')
# C é a variante que você criou, ou seja, pode ser ter o nome que você desejar. 
# O que você quer que repita deve ficar sempre justificado ("dentro") em relação ao FOR.
# Quando você quiser que pare, no exemplo o 'print("Fim")', o código deve ficar na mesma linha que o FOR.
#Por exemplo: Nós queremos que o programa repita a palavra "Oi" 10 vezes. Ao invés de digitar o código: print("Oi") as 10 vezes, nós apenas digitamos o código:
#for c in range(0,10):
#    print('Oi')
#print('Fim')
# Outro exemplo:
#n = int(input('Digite um numero: '))
#for c in range(0, n+1):
#    print(c)
#print('FIM')
# Mais um exemplo:
#i = int(input('Inicio: '))
#f = int(input('Final: '))
#p = int(input('Passo: '))
#for c in range(i, f+1, p):
#    print(c)
#print('Fim')
# Importante lembrar que o Python não conta a última casa, então se pedir para ele repetir (1,10) ele irá escrever 9 e não 10 vezes. Se você quiser contar de forma decrescente você deve adicionar o -1 no final, dentro dos parenteses (10,1,-1).
# Outro adendo importante é que junto ao FOR você pode agrupar outros comando, como o IF, INPUT, etc. dando uma condição que você deseja que aconteça em determinado momento.
#Por exemplo: 
#for c in range(0,5):
#    n = int(input("Digite um número: "))
#print("FIM")
# Outro exemplo:
#s = 0
#for c in range(0,5):
#    n = int(input('Digite um valor: '))
#    s = s + n
#print(f"O somatório de todos os valores é {s}")
#n = int(input('Digite um número:'))
#tot = 0
#for c in range(1, n+1):
#    if n % c == 0:
#        print(f"Este é um número primo: {c}")
#        tot = tot +1
#    else:
#        print(f"Este número não é primo: {c}")    
#print(f'O número {n} foi divisível {tot} vezes')

#def conteudo_gc(sequencia):
#    '''Calcula a quantidade de G e C na sequencia'''
#    sequencia = sequencia.upper()
#    '''Padroniza tudo em maiúsculo'''
#    g_count = sequencia.count('G')
#    '''Conta a quantidade de G'''
#    c_count = sequencia.count('C')
#    '''Conta a quantidade de c'''

#    total_gc = g_count + c_count
#    '''Aprensa a soma de G e C'''
#    porcentagem_gc = total_gc / len(sequencia)
#    '''Dia a % de GC na sequencia'''

#    return porcentagem_gc
#minha_dna = str(input('Digite a sequência desejada: '))
#valor_final = conteudo_gc(minha_dna)

#print(f'O contepudo GC da sequencia é: {valor_final:.2%}')

#def analisar_dna(sequencia):
#    sequencia = sequencia.upper()
#    sequencia_transcrita = sequencia.replace("T", "U")
#    inicio_sequencia = sequencia.startswith("ATG")
#    return sequencia_transcrita, inicio_sequencia

#dna = str(input('Digite a sequencia de DNA #desejada: '))

#meu_dna = analisar_dna(dna)

#print(f'o resultado da analise foi: {meu_dna}')

#genes_amostra = ["GAPDH", "BRCA1", "TP53", "EGFR", "MYC"]

#gene_alvo = "TP53"
#if gene_alvo in genes_amostra:
    #posicao = genes_amostra.index(gene_alvo)
    #print(f"O gene alvo '{gene_alvo}' se encontra #na posição {posicao} da sequência")
#else:
    #print(f"O gene alvo {gene_alvo} não foi #encontrado na sequência")

# =================================================================
# EXERCÍCIO: QUEM FOI O VENCEDOR?
# =================================================================

# Abaixo temos a lista de corredores na ordem em que cruzaram a meta.
# O primeiro da lista é o Medalha de Ouro, o segundo Prata, etc.
''' chegadas = ["Ana", "Bruno", "Catarina", "Diogo", "Elena", "Fábio"]

def verificar_podio(nome_corredor, lista_chegadas):
    """
    Esta função deve:
    1. Verificar SE o corredor está na lista.
    2. Se estiver, usar o .index() para descobrir a posição.
    3. Retornar uma mensagem personalizada:
       - Se posição for 0: "Medalha de Ouro! 🥇"
       - Se posição for 1: "Medalha de Prata! 🥈"
       - Se posição for 2: "Medalha de Bronze! 🥉"
       - Se for maior que 2: "Ficou em Xº lugar (fora do pódio)."
       - Se não estiver na lista: "Corredor não encontrado."
    """
    # TODO: Implementa a lógica aqui
    if nome_corredor in lista_chegadas:
        posicao = lista_chegadas.index(nome_corredor)
        if posicao == 0:
            return "Medalha de Ouro! 🥇"
        elif posicao == 1:
            return "Medalha de Prata! 🥈"
        elif posicao == 2:
            return "Medalha de Bronze! 🥉"
        else:
            return  f"Ficou em {posicao+1}º lugar (fora do pódio)."
    else:
        return "Corredor não encontrado"
# --- TESTES ---
# Tenta mudar os nomes abaixo para testar a tua função:
print(f"Resultado da Elena: {verificar_podio('Elena', chegadas)}")
print(f"Resultado do Ana: {verificar_podio('Ana', chegadas)}")
print(f"Resultado do Fábio: {verificar_podio('Fábio', chegadas)}")'''

# --- DESAFIO EXTRA (BIOINFORMÁTICA) ---
# Se tivesses uma lista de 1000 sequências de DNA e quisesses saber 
# se a sequência "ATGC" está entre as 10 primeiras, como usarias 
# o .index() para validar isso?
''' lista_dna = ["AGTC", "GCAT", "TAGC", "ATGC", "GCAA", "CTGA", "TGGC", "GCAT", "AATG", "ACCG", "TTGC", "TAAG", "AACT", "ATGG", "GGAC", "TTAG", "GCAT"]
if "ATGC" in lista_dna:
    posicao = lista_dna.index("ATGC")
    if posicao < 10:
        print("A sequencia está entre as 10 mais frequentes")
    else:
        print("A sequencia não se encontra entre as 10 primeiras")
else:
    print("A sequencia não foi encontrada na lista") '''
