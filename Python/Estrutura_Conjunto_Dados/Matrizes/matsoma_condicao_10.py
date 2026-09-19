# Algoritmo cria matriz 4x4 e verifica se os elementos são maiores que 10 e adiciona 2 caso sejam.

num = [[0 for j in range(4)] for i in range(4)]
# Cria uma matriz 4x4 inicializada com zeros.
# Usa list comprehension: para cada linha (i) cria uma lista de 4 elementos (j), todos iguais a 0.

for i in range(4):  # percorre as linhas da matriz
    for j in range(4):  # percorre as colunas da matriz
        num[i][j] = float(input(f"Digite o elemento MA[{i+1},{j+1}]: "))
        # Lê um valor do usuário, converte para float e armazena na posição [i][j] da matriz.
        
        if num[i][j] > 10:
            num[i][j] += 2
            # Se o valor digitado for maior que 10, soma 2 ao elemento.

print("\nMatriz resultante:")
# Exibe título antes de imprimir a matriz.

for i in range(4):  # percorre cada linha da matriz
    for j in range(4):  # percorre cada coluna da matriz
        print(f"{num[i][j]:.2f}", end=" ")
    print()  # Imprime uma nova linha após cada linha da matriz.
    # Imprime o elemento formatado com duas casas decimais.
    # Usa " " para adicionar um espaço entre os elementos.