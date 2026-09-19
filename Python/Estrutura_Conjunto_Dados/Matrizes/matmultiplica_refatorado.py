# Algoritmo para multiplicar uma matriz por um número inteiro

# Preenche a matriz diretamente com list comprehension
MA = [[int(input(f"Digite o elemento MA[{i+1},{j+1}]: ")) for j in range(5)] for i in range(5)]
# Aqui usamos list comprehension dupla:
# - O laço externo percorre as linhas (i de 0 a 4).
# - O laço interno percorre as colunas (j de 0 a 4).
# Para cada posição [i][j], o programa pede ao usuário um número inteiro
# e já monta a matriz MA completa sem precisar inicializar com zeros antes.

# Lê o número inteiro para multiplicar
n = int(input("Digite o número inteiro para multiplicar a matriz: "))
# Solicita ao usuário o número inteiro que será usado como fator de multiplicação.

# Cria a matriz resultante multiplicada
MR = [[MA[i][j] * n for j in range(5)] for i in range(5)]
# Outra list comprehension dupla:
# - Percorre cada elemento da matriz MA.
# - Multiplica pelo número n.
# - Armazena o resultado na matriz MR, que é a matriz resultante.

# Exibe a matriz resultante
print("Matriz resultante MR:")
for linha in MR:
    print(" ".join(str(elem) for elem in linha))
# Percorre cada linha da matriz MR.
# " ".join(...) transforma os elementos da linha em strings e os junta separados por espaço.
# Isso imprime a matriz de forma organizada, linha por linha.

