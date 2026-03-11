# =================================================================
# LISTA DE EXERCÍCIOS INTEGRADOS - DO BÁSICO AO AVANÇADO
# =================================================================

# 1. FUNÇÕES E NÚMEROS (Tópicos 1 e 2)
def calcular_tm(sequencia):
    """
    Calcula a Temperatura de Fusão (Tm) aproximada de um primer.
    Fórmula simples: Tm = (A+T) * 2 + (G+C) * 4
    """
    # Dica: usa os métodos .count('A'), .count('T'), etc.
    sequencia = sequencia.upper()
    a = sequencia.count("A")
    c = sequencia.count("C")
    t = sequencia.count("T")
    g = sequencia.count("G")

    tm = (a + t) * 2 + (g + c) * 4
    return tm
# 2. CONDICIONAIS E STRINGS (Tópicos 3 e 6)
def validar_dna(sequencia):
    """
    Retorna True se a sequência contiver apenas A, T, C, G.
    Caso contrário, retorna False.
    """
    validos = "ATCG"
    sequencia = sequencia.upper()
    for base in sequencia:
        if base not in validos:
            return False
    return True

# 3. LISTAS E INDEXING (Tópico 4)
def encontrar_start_codon(dna_lista):
    """
    Dada uma lista de sequências, retorna o índice da primeira 
    sequência que começa com 'ATG'. Se não encontrar, retorna -1.
    """
    for i, seq in enumerate(dna_lista):
        if seq.upper().startwith("ATG"):
            return i
    return -1

# 4. LOOPS E LIST COMPREHENSIONS (Tópico 5)
def filtrar_sequencias_longas(lista_seq, tamanho_min):
    """
    Usa List Comprehension para retornar apenas as sequências 
    que têm comprimento maior ou igual a tamanho_min.
    """
    return [s for s in lista_seq if len(s) >= tamanho_min]

# 5. DESAFIO FINAL (INTEGRAÇÃO TOTAL)
def relatorio_genomico(amostras):
    """
    Recebe um DICIONÁRIO onde a chave é o nome da amostra e o 
    valor é a sequência de DNA.
    Deve imprimir:
    - O nome da amostra
    - O tamanho da sequência
    - Se a sequência é válida (usa a função do exercício 2)
    - A Tm (usa a função do exercício 1)
    """
    print("--- RELATÓRIO DE ANÁLISE ---")
    for nome, seq in amostras.items():
        status = "Válido" if validar_dna(seq) else "Inválido"
        tm = calcular_tm(seq) if validar_dna(seq) else "N/A"
        
        print(f"Amostra: {nome}")
        print(f"   > Tamanho: {len(seq)}")
        print(f"   > Status: {status}")
        print(f"   > Tm estimado: {tm}°C")
        print(f"=-"*20)

    
# --- ESPAÇO PARA O TESTE DA RESOLUÇÃO DOS DESAFIOS --- #
# EXERCÍCIO 1 #
''' def calcular_tm(sequencia):
    sequencia = sequencia.upper()
    a = sequencia.count("A")
    c = sequencia.count("C")
    t = sequencia.count("T")
    g = sequencia.count("G")

    tm = (a + t) * 2 + (g + c) * 4
    return tm

teste_1 = "ATGC"
resultado_1 = calcular_tm(teste_1)

print(f"Sequência = {teste_1}")
print(f"Resultado do Python = {resultado_1}")

if resultado_1 == 12:
    print("✅ Teste 1 passou!")
else:
    print("❌ Teste 1 falhou!") '''

# EXERCÍCIO 2 #
''' def validar_dna(sequencia):
    validos = "ATCG"
    sequencia = sequencia.upper()
    for base in sequencia:
        if base not in validos:
            return False
    return True

teste_1 = 'aucg'
resultado_1 = validar_dna(teste_1)
print(f'Sequência = {teste_1}')
print(f'A sequência apresenta apenas Bases de DNA? {resultado_1}')

teste_2 = 'atgc'
resultado_2 = validar_dna(teste_2)
print(f'Sequência = {teste_2}')
print(f'A sequência apresenta apenas Bases de DNA? {resultado_2}') '''

# EXERCÍCIO 3 #
''' def encontrar_start_codon(dna_lista):
    for i, seq in enumerate(dna_lista):
        if seq.upper().startswith("ATG"):
            return i
    return -1

lista_a = ["GCTA", "ATGCG", "CCAA"]
res_a = encontrar_start_codon(lista_a)
print(f"Teste A - Esperado: 1 | Obtido: {res_a}")

lista_b = ["ATGGGG", "TTTAAA", "GGCC"]
res_b = encontrar_start_codon(lista_b)
print(f"Teste B - Esperado: 0 | Obtido: {res_b}")

lista_c = ["GCTA", "CCAA", "TTTT"]
res_c = encontrar_start_codon(lista_c)
print(f"Teste C - Esperado: -1 | Obtido: {res_c}")

if res_a == 1 and res_b == 0 and res_c == -1:
    print("\n✅ TUDO CORRETO! A tua função identifica os índices perfeitamente.")
else:
    print("\n❌ Algo falhou. Verifica se usaste o .startswith() corretamente.") '''

# EXERCÍCIO 4 #
''' def filtrar_sequencias_longas(lista_seq, tamanho_min):
    return [s for s in lista_seq if len(s) >= tamanho_min]

seq_teste = ["ATGC", "ATGCATGCAT", "GC", "ATGCAT"]
res_teste = filtrar_sequencias_longas(seq_teste, 5)

print(f"Lista original = {seq_teste}")
print(f"Resultado (tamanho mínimo = 5) = {res_teste}")

esperado = ["ATGCATGCAT", "ATGCAT"]
if res_teste == esperado:
    print("\n✅ TUDO CERTO!!! A List Comrpehension filtrou perfeitamente")
else:
    print("\n❌ ALGO DEU ERRADO!!! Verifique se o sinal '>=' foi usado corretamente ou se há outro erro no código") '''

# EXERCÍCIO 5 #
''' def relatorio_genomico(amostras):
    for nome, seq in amostras.items():
        eh_valida = validar_dna(seq)
        status = "Válido" if eh_valida else "Inválido"
        tm = calcular_tm(seq) if eh_valida else "N/A"
            
    print(f"Amostra: {nome}")
    print(f"   > Tamanho: {len(seq)}")
    print(f"   > Status: {status}")
    print(f"   > Tm estimado: {tm}°C")
    print(f"=-"*20)

meus_dados = {
    "Amostra_A": "ATGCGTACTA",
    "Amostra_B": "GCTAGCTX",
    "Amostra_C": "ATATATAT"
    }
print("Iniciando teste do relatório...")

amostras = meus_dados
for nome, seq in amostras.items():
    eh_valida = validar_dna(seq)
    status = "Válido" if eh_valida else "Inválido"
    tm = calcular_tm(seq) if eh_valida else "N/A"
    print(f"Amostra: {nome}")
    print(f"  > Tamanho: {len(seq)}")
    print(f"  > Status: {status}")
    print(f"  > Tm estimado: {tm}°C")
    print(f"=-"*20) '''

# REVISÃO SEMANAL: PYTHON & LÓGICA
#Instruções: Preencha as funções e variáveis onde está escrito '___' ou 'pass'.

# 1. STRINGS E COMPRIMENTO (len)
# Preencha os valores que você acredita que o len() retornará

s1 = "Python é legal"
s2 = "ab\ncd"
s3 = "c:\\users\\user"

# Substitua o None pelo seu palpite
comprimento_s1 = 14
comprimento_s2 = 5 #o \n conta apenas como 1 caracter'''
comprimento_s3 = 13 # o par \\ conta apenas como uma única barra

# 2. MANIPULAÇÃO DE LISTAS (O desafio do Luigi)
# Objetivo: Retornar nomes de quem ficou em 1º lugar.

def filtrar_vencedores(corredores):
    """
    Recebe uma lista de dicionários e retorna uma lista de nomes
    de quem tem 'finish' igual a 1. Ignore quem não tem nome (None).
    """
    vencedores = []
    # ESCREVA SEU CÓDIGO AQUI
    for c in corredores: #seleciona os corredores
        if c ['finish'] == 1: #seleciona apenas aquele que chegou em 1° lugar
            if c ['name'] is not None: #verifica se o nome não é nulo
                vencedores.append(c['name']) #adiciona o nome a lista final de nomes desejada
    return vencedores

# Teste para a função acima:
dados_mario_kart = [
    {'name': 'Peach', 'finish': 3},
    {'name': 'Bowser', 'finish': 1},
    {'name': None, 'finish': 1},
    {'name': 'Toad', 'finish': 1},
]

# 3. BIBLIOTECAS (math)
# Objetivo: Praticar importação e uso de funções externas.

# IMPORTA O MATH COMO 'mt' AQUI
import math as mt

def calcular_fatorial_de_cinco():
    # Use a função fatorial da biblioteca math
    resultado = mt.factorial(5)
    return 0

# 4. DESAFIO BLACKJACK (Sobrecarga de Lógica)
# Objetivo: Calcular pontos sem estourar 21.

def calcular_pontos(mao):
    """
    'J', 'Q', 'K' valem 10. 'A' vale 11. Números valem o valor facial.
    Retorne 0 se a soma passar de 21.
    """
    total = 0
    # ESCREVA SEU CÓDIGO AQUI (Dica: use um loop for na mão)
    for carta in mao:
        if carta in ['J', 'Q', 'K']:
            total += 10
        elif carta == 'A':
            total += 11
        else:
            total += int(carta)
    if total > 21:
        return 0
    return total

# DESAFIO FINAL: ANALISADOR DE ESTOQUE
#Objetivo: Trabalhar com dicionários aninhados dentro de listas.

# Uma lista de produtos, onde cada produto é um dicionário.
estoque = [
    {"nome": "Teclado", "preco": 150, "quantidade": 5},
    {"nome": "Mouse", "preco": 80, "quantidade": 0},
    {"nome": "Monitor", "preco": 900, "quantidade": 2},
    {"nome": "Fone", "preco": 200, "quantidade": 10},
]

def analisar_estoque(lista_produtos):
    """
    Esta função deve retornar um dicionário com:
    1. 'valor_total_estoque': Soma de (preco * quantidade) de todos os itens.
    2. 'itens_esgotados': Uma lista com os NOMES dos produtos que têm quantidade 0.
    """
    relatorio = {
        "valor_total_estoque": 0,
        "itens_esgotados": []
    }
    
    # ESCREVA SEU CÓDIGO AQUI
    # Dica: Use um loop 'for' para percorrer a lista_produtos
    
    return relatorio

# --- TESTE ---
if __name__ == "__main__":
    resultado = analisar_estoque(estoque)
    print("--- Relatório de Estoque ---")
    print(f"Valor Total em R$: {resultado['valor_total_estoque']}") # Esperado: 2750
    print(f"Produtos Esgotados: {resultado['itens_esgotados']}")     # Esperado: ['Mouse']

# AREA DE TESTES (Não mexa aqui, apenas execute o arquivo)
# 
if __name__ == "__main__":
    print("--- Resultados dos Testes ---")
    
    # Teste 1
    ''' comprimento_s1 = 14
    comprimento_s2 = 5
    comprimento_s3 = 13 '''
    # Teste 2
    ''' res_vencedores = filtrar_vencedores(dados_mario_kart)
    print(f"Vencedores encontrados: {res_vencedores}") # Esperado: ['Bowser', 'Toad']'''
    
    # Teste 3
    ''' import math as mt
    def calcular_fatorial_de_cinco():
        return mt.factorial(5)
    resultado = calcular_fatorial_de_cinco()
    
    print(resultado) '''

    # Teste 4
    ''' mao_teste = ['J', 'A', '2'] # 10 + 11 + 2 = 23 (Estourou!)
    print(f"Pontos da mão {mao_teste} | total =  {calcular_pontos(mao_teste)}") # Esperado: 0 ''' 

    # Teste DESAFIO