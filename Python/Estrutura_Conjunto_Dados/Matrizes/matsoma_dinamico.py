# Algoritmo para calcular a soma, média, maior e menor elemento de uma matriz de dimensão NxM. 

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

# Preenche a matriz com validação
num = [[ler_float(f"Digite o elemento MA[{i+1},{j+1}]: ") for j in range(colunas)] for i in range(linhas)]
# cria a matriz usando list comprehension:
# - percorre cada linha (i)
# - percorre cada coluna (j)
# - chama a função ler_float para garantir que o valor digitado seja válido

# Calcula estatísticas
todos = [elem for linha in num for elem in linha]  # "achata" a matriz em uma lista única
soma = sum(todos)  # soma de todos os elementos
media = soma / len(todos)  # média aritmética
maximo = max(todos)  # maior valor
minimo = min(todos)  # menor valor

# Exibe os resultados
print(f"\nA soma dos elementos da matriz é: {soma:.2f}")
print(f"A média dos elementos da matriz é: {media:.2f}")
print(f"O maior elemento da matriz é: {maximo:.2f}")
print(f"O menor elemento da matriz é: {minimo:.2f}")

# Exibe a matriz com linhas de grade
print("\nMatriz digitada:")
largura = 10  # largura fixa para cada célula

def linha_horizontal():
    print("+" + "+".join("-" * largura for _ in range(colunas)) + "+")
# função auxiliar que imprime uma linha horizontal da tabela
# cada célula é representada por "-" repetido conforme a largura
# os blocos são separados por "+"

linha_horizontal()  # imprime a linha superior da tabela
for linha in num:  # percorre cada linha da matriz
    print("|" + "|".join(f"{elem:^{largura}.2f}" for elem in linha) + "|")
    # imprime os elementos da linha, centralizados dentro da largura fixa
    # cada célula é separada por "|"
    linha_horizontal()  # imprime a linha de grade abaixo da linha de dados

'''
Digite o número de linhas da matriz: 4
Digite o número de colunas da matriz: 4
Digite o elemento MA[1,1]: 12,8
Digite o elemento MA[1,2]: 158,6
Digite o elemento MA[1,3]: 123,87
Digite o elemento MA[1,4]: 2,35
Digite o elemento MA[2,1]: 4,89
Digite o elemento MA[2,2]: 558,69
Digite o elemento MA[2,3]: 33,1
Digite o elemento MA[2,4]: 12,9
Digite o elemento MA[3,1]: 38,99
Digite o elemento MA[3,2]: 40,87
Digite o elemento MA[3,3]: 358,97
Digite o elemento MA[3,4]: 357,56
Digite o elemento MA[4,1]: 487
Digite o elemento MA[4,2]: 458
Digite o elemento MA[4,3]: 498,21
Digite o elemento MA[4,4]: 500,01

A soma dos elementos da matriz é: 3646.81
A média dos elementos da matriz é: 227.93
O maior elemento da matriz é: 558.69
O menor elemento da matriz é: 2.35

Matriz digitada:
+----------+----------+----------+----------+
|  12.80   |  158.60  |  123.87  |   2.35   |
+----------+----------+----------+----------+
|   4.89   |  558.69  |  33.10   |  12.90   |
+----------+----------+----------+----------+
|  38.99   |  40.87   |  358.97  |  357.56  |
+----------+----------+----------+----------+
|  487.00  |  458.00  |  498.21  |  500.01  |
+----------+----------+----------+----------+

'''