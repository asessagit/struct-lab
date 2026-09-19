# Algoritmo cria matriz 4x4 e verifica se os elementos são maiores que 10 e adiciona 2 caso sejam.
# Além disso, calcula soma, média, máximo e mínimo dos elementos.

num = [[0 for j in range(4)] for i in range(4)]
# Cria uma matriz 4x4 inicializada com zeros usando list comprehension.

for i in range(4):  # percorre as linhas da matriz
    for j in range(4):  # percorre as colunas da matriz
        num[i][j] = float(input(f"Digite o elemento MA[{i+1},{j+1}]: "))
        # Lê um valor do usuário, converte para float e armazena na posição [i][j].
        
        if num[i][j] > 10:
            num[i][j] += 2
            # Se o valor digitado for maior que 10, soma 2 ao elemento.

# "Achata" a matriz em uma lista única para facilitar cálculos
todos = [elem for linha in num for elem in linha]

# Calcula estatísticas
soma = sum(todos)        # soma de todos os elementos
media = soma / len(todos)  # média aritmética
maximo = max(todos)      # maior valor
minimo = min(todos)      # menor valor

# Exibe os resultados
print(f"\nA soma dos elementos da matriz é: {soma:.2f}")
print(f"A média dos elementos da matriz é: {media:.2f}")
print(f"O maior elemento da matriz é: {maximo:.2f}")
print(f"O menor elemento da matriz é: {minimo:.2f}")

print("\nMatriz resultante:")
# Exibe título antes de imprimir a matriz.

for i in range(4):  # percorre cada linha da matriz
    for j in range(4):  # percorre cada coluna da matriz
        print(f"{num[i][j]:.2f}", end=" ")
        # Imprime o elemento formatado com duas casas decimais.
        # Usa " " para adicionar um espaço entre os elementos.
    print()  # Quebra de linha ao final de cada linha da matriz.
