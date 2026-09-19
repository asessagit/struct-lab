# Função para calcular a média de uma lista de números
def calcular_media(numeros):
    if not numeros:  # verifica se a lista está vazia
        return 0  # retorna 0 para evitar divisão por zero
    
    soma = sum(numeros)  # soma todos os números da lista
    media = soma / len(numeros)  # calcula a média dividindo pela quantidade de elementos
    
    return media  # retorna o valor da média

# Main program
quantidade = int(input("Digite a quantidade de números para calcular a média: "))
numeros = []  # lista para armazenar os números digitados
for i in range(quantidade):
    numero = float(input(f"Digite o número {i + 1}: "))  # lê cada número como float
    numeros.append(numero)  # adiciona o número à lista

media = calcular_media(numeros)  # chama a função para calcular a média
print(f"A média dos números é: {media:.2f}")  # exibe o resultado formatado 
