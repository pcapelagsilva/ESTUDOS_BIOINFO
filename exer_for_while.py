# EXERCÍCIO DE REPETIÇÃO 'FOR' - 1º Exercício
'''num = float(input('Digite um número: '))

print('A tabuada do número escolhido é:')
for tabuada in range(1,11):
    tabuada = num * tabuada
    print(f"{tabuada}", end=' | ')'''

# EXERCÍCIO DE REPETIÇÃO 'FOR' - 2º Exercício
'''soma = 0
impar = par = 0

for pa in range (1, 501, 2):
    if pa % 3 == 0:
        soma += pa
print(f"A soma de todos os números impares de 1 a 500 é igual a: {soma}")'''

# EXERCÍCIO DE REPETIÇÃO 'FOR' - 3º Exercício
'''maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Escreva o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso registrado foi {maior}Kg')
print(f'O menor peso registrado foi {menor}Kg')'''

# EXERCÍCIO DE REPETIÇÃO 'FOR' - 4º Exercício
''' frase = str(input('Digite uma frase: ')) # Define a frase desejada através de uma pergunta'''

'''junto = ''.join(frase) # Define o conjunto 'Junto', que ira tirar os espaços da frase'''

'''inverso = '' # Define o conjunto 'Inverso', que represnta a frase escrita ao contrário'''

# O loop 'for' irá percorrer a frase de trás para frente
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de "{frase}" é igual a "{inverso}"')
if inverso == junto:
    print('Temo um palíndromo!!!')
else:
    print('A frase digitada não é um palíndromo...')'''
# EXERCÍCIO DE REPETIÇÃO 'FOR' - 5º Exercício
''' num  = int(input('Digite um número: ')) # Entrada de dados

if num > 1: # Primeira condição para ser primo, números menores ou iguais a 1 não são primos por definição
    for p in range(2, int(num / 2) + 1): # Cria o laço de repetição. 
    # Dentro dos parenteses o primeiro 2 indica para ele iniciar por esse número.
    # O num/2 serve para indicar que nenhum número pode ser dividido por algo maior que a sua metade (exceto por ele mesmo).
        if num % p == 0:
        # O simbolo % calcula o resto da divisão.
        # num % p == 0, significa que a divisão é exata, ou seja, se o número for divisível por qualquer p nesse intervalo ele não é primo.
            print(f"O número {num} não é primo...")

    else:
        print(f"O número {num} é primo!!!")
else:
        print(f'O número {num} não é primo...') '''

# EXERCÍCIO DE REPETIÇÃO 'FOR' - 6º Exercício
''' from datetime import date # Importou a data atual
maior = 0 # Deu um ponto de partida para o grupo maior de idade
menor = 0 # Deu um ponto de partida para o grupo menor de idade
hoje  = date.today().year # Define o ano atual, cada parte significa:
# date = classe lida com operações de calendáro
# .today() = é o que solicita ao computador a data completa
# .year = cria um filtro para separar apenas o ano desse arquivo (data)
# hoje = nome dado ao grupo onde se encontra a informação do ano

for c in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = hoje - ano

    if ano >= 21:
        maior += 1
    else:
        menor+= 1
print(f'No total {maior} pessoas são maiores de idade (+21 anos)')
print(f'No total {menor} pessoas são menores de idade') '''

# EXERCÍCIO DE REPETIÇÃO 'WHILE' - 1º Exercício
''' sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos... Por favor, informe seu sexo novamente [M/F]: ')).upper()
print('Seus dados estão sendo registrados...')
print('Seus dados foram registrados com sucesso!!') '''

# EXERCÍCIO DE REPETIÇÃO 'WHILE' - 2º Exercício

''' n1 = int(input('Digite um número: ')) ''' # escolha do primeiro número
''' n2 = int(input("Digite outro número: ")) '''# escolha do segundo número
''' opcao = 0 '''# definindo um valor para o grupo 'opcao'

'''while opcao != 5:''' #enquanto 'opcao' for diferente de 5 mostrar as opções
    #print('''    [1] Somar
    #[2] Multiplicar
    #[3] Maior
    #[4] Novos números
    #[5] Sair do programa''')
'''    opcao = int(input('Qual sua opção? ')) # escolhendo um valor para 'opcao'

    if opcao == 1: # condição 'se'
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}')
    elif opcao == 2: # junção das condições 'se' e 'senão' sempre utilizada entre o 'if' e o 'else'
        print(f'A multiplicação de {n1} e {n2} é igual a {n1*n2}')
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f'Entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        print('Informe novos números')
        n1 = int(input('Digite um número: '))
        n2 = int(input("Digite outro número: "))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida... tente novamente.')'''

# EXERCÍCIO DE REPETIÇÃO 'WHILE' - 3º Exercício
''' valor = float(input('Qual valor você deseja sacar? R$')) # perguntado o valor que o cliente deseja
total = valor # representa o que ainda falta ser pagp
cedula = 50 # define o maior valor para se iniciar
sacar = 0 # defina quantas notas serão entregue de cada valor

while True:
    # tenta tirar a notal atual (50) do valor total
    if total >= cedula:
        total -= cedula
        sacar += 1
    else:
        # se não der mais de tirar essa nota, imprime o resultado
        if sacar > 0:
            print(f'Total de {sacar} cédulas de R${cedula}')
        # troca para a nota menor
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        # reseta o contador de nota para a nova cédula
        valor = 0
        # se o valor chegou a zero, interrompe o loop
        if total == 0:
            break '''

# EXERCÍCIO DE REPETIÇÃO 'WHILE' - 4º Exercício
