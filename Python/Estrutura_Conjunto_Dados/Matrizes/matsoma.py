#Algoritmo para calcular a soma de uma matriz de dimensão 2:4
num = [[0 for i in range(2)] for j in range(4)] # Matriz de dimensão 4x2
soma = 0 # Variável para armazenar a soma dos elementos
for i in range(4): # Loop para percorrer as linhas da matriz
    for j in range(2): # Loop para percorrer as colunas da matriz
        num[i][j] = float(input(f"Digite o elemento:"))   # Solicita ao usuário que digite o elemento da matriz
        soma += num[i][j] # Adiciona o elemento digitado à soma total
print(f"A soma dos elementos da matriz é: {soma}") # Exibe a soma total dos elementos da matriz