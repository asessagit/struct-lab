# Função que encontra o número com o maior módulo (valor absoluto) em um vetor
def MaiorModulo(VetNum):
    # VetNum recebe os valores de VetInicial
    if VetNum is None or len(VetNum) == 0:
        # Verifica se o vetor não foi fornecido ou está vazio

        print("Erro: O vetor está vazio ou não foi fornecido.")
        return None, None, None
    
    if len(VetNum) == 1:
        # Se houver apenas um elemento, ele é o maior módulo por definição
        return VetNum[0], abs(VetNum[0]), 0  # Retorna o único número, seu módulo e o índice 0. 
    
    maior = VetNum[0]       # Inicializa o maior com o primeiro elemento
    indice_maior = 0        # Guarda o índice do maior módulo
    
    for i in range(1, len(VetNum)):  # percorre o vetor a partir do segundo elemento
        if abs(VetNum[i]) > abs(maior):
            maior = VetNum[i]        # atualiza o maior
            indice_maior = i         # atualiza o índice
    
    return maior, abs(maior), indice_maior  # retorna número, módulo e índice

# Main program
entrada = input("Digite os números separados por espaço: ").split()
# Lê uma linha de entrada e separa os valores por espaço

VetInicial = []  # lista para armazenar os números validados
for elemento in entrada:
    try:
        VetInicial.append(float(elemento.replace(",", ".")))  # converte cada item para float
    except ValueError:
        print(f"Erro: '{elemento}' não é um número válido. Ignorado.")
        # se algum elemento não for número, mostra erro e ignora

M, Modulo, Indice = MaiorModulo(VetInicial)  # chama a função para encontrar o maior módulo
if M is not None:
    print(f"\nO número com maior módulo é: {M}")
    print(f"O valor absoluto (módulo) é: {Modulo}")
    print(f"O índice do número no vetor é: {Indice}")

    # Exibe os números em ordem crescente e decrescente
    print(f"\nNúmeros em ordem crescente: {sorted(VetInicial)}")
    print(f"Números em ordem decrescente: {sorted(VetInicial, reverse=True)}")



'''
1. A função agora retorna duas informações:
    O número original com maior módulo.
    O valor absoluto desse número.
    O índice (posição) do número dentro do vetor.
    A lista de números em ordem crescente e decrescente.

2. Entradas inválidas são ignoradas com mensagem de erro.
3. Aceita int e float (inclusive com vírgula como separador decimal).

Exenplo de entradas e saídas:

Digite os números separados por espaço: 1 2 3 abc 7
Erro: 'abc' não é um número válido. Ignorado.

O número com maior módulo é: 7.0
O valor absoluto (módulo) é: 7.0
O índice do número no vetor é: 3

Digite os números separados por espaço: 54,4 60 72 1,2 -58,5 -5 -7     

O número com maior módulo é: 72.0
O valor absoluto (módulo) é: 72.0
O índice do número no vetor é: 2

Números em ordem crescente: [-58.5, -7.0, -5.0, 1.2, 54.4, 60.0, 72.0]
Números em ordem decrescente: [72.0, 60.0, 54.4, 1.2, -5.0, -7.0, -58.5]

***VetNum só existe dentro da função. O nome
VetInicial poderia ser alterado para VetNum,
mas não é necessário; manter nomes diferentes ajuda
a distinguir o programa principal do parâmetro da função.
'''
