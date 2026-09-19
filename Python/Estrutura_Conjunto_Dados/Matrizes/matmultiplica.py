#Algoritimo para multiplicar uma matriz por um número inteiro
from ast import For


MA = [[0] *5 for i in range(5)]
MR = [[0] *5 for i in range(5)]
n = 0
i = 0
j = 0
for i in range(5):
    for j in range(5):
        MA[i][j] = int(input(f"Digite o elemento MA[%d,%d]: " % (i+1, j+1)))
n = int(input("Digite o número inteiro para multiplicar a matriz: "))
for i in range(5):
    for j in range(5):
        MR[i][j] = MA[i][j] * n
print("Matriz resultante MR:")
for i in range(5):
    for j in range(5):
        print(MR[i][j], end=" ")
    print()
