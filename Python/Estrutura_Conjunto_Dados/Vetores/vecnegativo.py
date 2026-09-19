# Algoritmo para encontrar valores negativos e substituir por 1
import random 

# Gera 10 números aleatórios entre -10 e 10
num = [random.uniform(-10, 10) for i in range(10)]

print("Números gerados:")
for i, valor in enumerate(num, start=1):
    print(f"Produto {i}: {valor:.2f}")   # mostra com 2 casas decimais

# Substitui negativos por 1
for i in range(10):
    if num[i] < 0:
        num[i] = 1

print("\nVetor final:")
for i, valor in enumerate(num, start=1):
    print(f"Produto {i}: {valor:.2f}")