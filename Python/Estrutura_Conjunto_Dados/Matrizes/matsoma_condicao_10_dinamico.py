# Matriz dinâmica: o usuário escolhe linhas e colunas, tornando o algoritmo mais flexível.
# Além disso, calcula soma, média, máximo e mínimo dos elementos.
# Função para ler um número real com validação
def ler_float(mensagem):
    while True:  # loop infinito até o usuário digitar corretamente
        valor = input(mensagem).strip()  # lê a entrada e remove espaços extras
        valor = valor.replace(",", ".")  # aceita vírgula como separador decimal, trocando por ponto
        try:
            return float(valor)  # tenta converter para número real (float)
        except ValueError:  # se não conseguir converter (entrada inválida)
            print("Entrada inválida! Digite apenas números reais (ex: 115.6).")
            # mostra mensagem de erro e volta ao início do loop

# Usuário define o tamanho da matriz
linhas = int(input("Digite o número de linhas da matriz: "))  # lê quantidade de linhas
colunas = int(input("Digite o número de colunas da matriz: "))  # lê quantidade de colunas

# Preenche a matriz com validação e aplica a regra (>10 soma 2)
num = []
for i in range(linhas):  # percorre cada linha
    linha = []
    for j in range(colunas):  # percorre cada coluna
        valor = ler_float(f"Digite o elemento MA[{i+1},{j+1}]: ")
        if valor > 10:
            valor += 2  # aplica a regra: se maior que 10, soma 2
        linha.append(valor)  # adiciona o valor na linha
    num.append(linha)  # adiciona a linha completa na matriz

# "Achata" a matriz em uma lista única para facilitar cálculos globais
todos = [elem for linha in num for elem in linha]

# Calcula estatísticas globais
soma = sum(todos)        # soma de todos os elementos
media = soma / len(todos)  # média aritmética
maximo = max(todos)      # maior valor
minimo = min(todos)      # menor valor

# Exibe os resultados globais
print(f"\nA soma dos elementos da matriz é: {soma:.2f}")
print(f"A média dos elementos da matriz é: {media:.2f}")
print(f"O maior elemento da matriz é: {maximo:.2f}")
print(f"O menor elemento da matriz é: {minimo:.2f}")

# Calcula soma por linha
print("\nSoma por linha:")
for i, linha in enumerate(num):
    print(f"Linha {i+1}: {sum(linha):.2f}")

# Calcula soma por coluna
print("\nSoma por coluna:")
for j in range(colunas):
    soma_coluna = sum(num[i][j] for i in range(linhas))
    print(f"Coluna {j+1}: {soma_coluna:.2f}")

# Exibe a matriz com linhas de grade
print("\nMatriz resultante:")
largura = 10  # largura fixa para cada célula

def linha_horizontal():
    print("+" + "+".join("-" * largura for _ in range(colunas)) + "+")
# função auxiliar que imprime uma linha horizontal da tabela

linha_horizontal()  # imprime a linha superior da tabela
for linha in num:  # percorre cada linha da matriz
    print("|" + "|".join(f"{elem:^{largura}.2f}" for elem in linha) + "|")
    linha_horizontal()  # imprime a linha de grade abaixo da linha de dados
    # cada célula é representada por "-" repetido conforme a largura

'''
Digite o número de linhas da matriz: 4
Digite o número de colunas da matriz: 4
Digite o elemento MA[1,1]: 11
Digite o elemento MA[1,2]: 11
Digite o elemento MA[1,3]: 11
Digite o elemento MA[1,4]: 11
Digite o elemento MA[2,1]: 11
Digite o elemento MA[2,2]: 11
Digite o elemento MA[2,3]: 11
Digite o elemento MA[2,4]: 11
Digite o elemento MA[3,1]: 11
Digite o elemento MA[3,2]: 11
Digite o elemento MA[3,3]: 11
Digite o elemento MA[3,4]: 11
Digite o elemento MA[4,1]: 11
Digite o elemento MA[4,2]: 11
Digite o elemento MA[4,3]: 11
Digite o elemento MA[4,4]: 11

A soma dos elementos da matriz é: 208.00
A média dos elementos da matriz é: 13.00
O maior elemento da matriz é: 13.00
O menor elemento da matriz é: 13.00

Soma por linha:
Linha 1: 52.00
Linha 2: 52.00
Linha 3: 52.00
Linha 4: 52.00

Soma por coluna:
Coluna 1: 52.00
Coluna 2: 52.00
Coluna 3: 52.00
Coluna 4: 52.00

Matriz resultante:
+----------+----------+----------+----------+
|  13.00   |  13.00   |  13.00   |  13.00   |
+----------+----------+----------+----------+
|  13.00   |  13.00   |  13.00   |  13.00   |
+----------+----------+----------+----------+
|  13.00   |  13.00   |  13.00   |  13.00   |
+----------+----------+----------+----------+
|  13.00   |  13.00   |  13.00   |  13.00   |
+----------+----------+----------+----------+
'''