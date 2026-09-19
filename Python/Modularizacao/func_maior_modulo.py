# Função que encontra o número com o maior módulo (valor absoluto) em um vetor
def MaiorModulo(VetNum):
    if VetNum is None or len(VetNum) == 0:
        # Verifica se o vetor não foi fornecido (None) ou está vazio.
        # Se estiver vazio, não há como calcular o maior módulo.
        print("Erro: O vetor está vazio ou não foi fornecido.")
        return  # encerra a função sem retornar valor válido
    
    if len(VetNum) == 1:
        # Caso o vetor tenha apenas um elemento, esse elemento é o maior módulo por definição.
        return VetNum[0]
    
    maior = VetNum[0]  # Inicializa o maior com o primeiro elemento do vetor
    
    for i in range(1, len(VetNum)):  # percorre o vetor a partir do segundo elemento
        if abs(VetNum[i]) > abs(maior):
            # Compara o valor absoluto do elemento atual com o maior encontrado até agora.
            # Se for maior, atualiza a variável 'maior'.
            maior = VetNum[i]
    
    return maior  # retorna o elemento com maior módulo

# Main program
VetInicial = list(map(int, input("Digite os números separados por espaço: ").split()))
# Lê uma linha de entrada do usuário.
# Usa split() para separar os números por espaço.
# Converte cada item para inteiro com map(int).
# Transforma o resultado em lista com list().

M = MaiorModulo(VetInicial)  # chama a função para encontrar o maior módulo
print(M)  # imprime o resultado

'''
Exemplos de entrada e saída:
Digite os números separados por espaço: 1 -1 5 -10 20
20

Digite os números separados por espaço: 1 5 6 -10 5 8 -100
-100

1. Lê uma lista de números inteiros digitados pelo usuário.

2. Verifica se a lista está vazia ou tem apenas um elemento.

3. Percorre todos os elementos e compara seus valores absolutos.

4. Retorna o número com maior módulo (positivo ou negativo).

'''
