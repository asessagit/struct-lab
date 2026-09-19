# Algoritmo para verififcar se um número é par e multiplicá-lo por 2
num = []
i = 0 
while True:
    valor = int(input("Digite um número (ou 0 para sair): "))
    if valor == 0:
        break
    num.append(valor)
for i in range(len(num)):
    if num[i] % 2 == 0:
        num[i] *= 2
print("Números processados:", num)