# Função para ler um número real ou inteiro com validação
def ler_numero(mensagem):
    while True:  # loop infinito até o usuário digitar corretamente
        valor = input(mensagem).strip()  # lê a entrada e remove espaços extras
        valor = valor.replace(",", ".")  # aceita vírgula como separador decimal
        try:
            numero = float(valor)  # tenta converter para float (aceita int e real)
            return numero  # retorna o número válido
        except ValueError:  # se não conseguir converter (entrada inválida)
            print("Erro: digite apenas números inteiros ou reais (ex: 10 ou 115.6).")
            # mostra mensagem de erro e volta ao início do loop

# Função para calcular estatísticas de uma lista de números
def calcular_estatisticas(numeros):
    if not numeros:  # verifica se a lista está vazia
        return 0, 0, 0, 0  # retorna valores neutros para evitar erros
    
    soma = sum(numeros)  # soma todos os números da lista
    media = soma / len(numeros)  # calcula a média
    maximo = max(numeros)  # maior número
    minimo = min(numeros)  # menor número
    
    return soma, media, maximo, minimo  # retorna todas as estatísticas

# Main program
quantidade = int(ler_numero("Digite a quantidade de números: "))
# lê a quantidade de números, validando que seja int

numeros = []  # lista para armazenar os números digitados
for i in range(quantidade):
    numero = ler_numero(f"Digite o número {i + 1}: ")  # lê cada número com validação
    numeros.append(numero)  # adiciona o número à lista

# Calcula estatísticas
soma, media, maximo, minimo = calcular_estatisticas(numeros)

# Exibe os resultados
print(f"\nSoma dos números: {soma:.2f}")
print(f"Média dos números: {media:.2f}")
print(f"Maior número: {maximo:.2f}")
print(f"Menor número: {minimo:.2f}")


'''
Exemplo de entrada e saída:

Digite a quantidade de números: 3
Digite o número 1: 11,11
Digite o número 2: 10,10
Digite o número 3: a2c
Erro: digite apenas números inteiros ou reais (ex: 10 ou 115.6).
Digite o número 3: 9,55

Soma dos números: 30.76
Média dos números: 10.25
Maior número: 11.11
Menor número: 9.55

1. Função ler_numero para validar entradas.

2. Aceita int (10) e float (12.5 ou 12,5).

3. Estatísticas completas: soma, média, máximo e mínimo.

4. Qualquer caractere inválido gera mensagem de erro e pede novamente.

5. Formatação com duas casas decimais para clareza.
'''
