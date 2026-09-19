# Algoritmo para multiplicar uma matriz por um número inteiro

# Usuário define o tamanho da matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# Preenche a matriz diretamente com list comprehension
MA = [[int(input(f"Digite o elemento MA[{i+1},{j+1}]: ")) for j in range(colunas)] for i in range(linhas)]

# Lê o número inteiro para multiplicar
n = int(input("Digite o número inteiro para multiplicar a matriz: "))

# Cria a matriz resultante multiplicada
MR = [[MA[i][j] * n for j in range(colunas)] for i in range(linhas)]

# Exibe a matriz resultante
print("\nMatriz resultante MR:")
for linha in MR:
    print(" ".join(str(elem) for elem in linha))
