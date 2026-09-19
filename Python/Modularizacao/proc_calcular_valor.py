# Procedimento para calcular o valor com desconto baseado em faixas de preço
def calcular_desconto(valor):
    if valor <= 100:
        desconto = 0
        # Se o valor for até 100, não há desconto (0%).
    elif valor <= 200:
        desconto = 0.1
        # Se o valor estiver entre 101 e 200, aplica 10% de desconto.
    else:
        desconto = 0.2
        # Se o valor for acima de 200, aplica 20% de desconto.
    
    valor_desconto = valor - (valor * desconto)
    # Calcula o valor final já com desconto aplicado.
    
    print(f"Valor original: {valor:.2f}, Desconto aplicado: {desconto*100:.0f}%, Valor com desconto: {valor_desconto:.2f}")
    # Exibe o valor original, a porcentagem de desconto e o valor final formatados.

# Main program
valor = float(input("Digite o valor do produto: "))
# Lê o valor do produto digitado pelo usuário e converte para float.

calcular_desconto(valor)
# Chama a função para calcular e mostrar o desconto com base no valor informado.

'''
Exemplo de entrada e saída:

Digite o valor do produto: 100
Valor original: 100.00, Desconto aplicado: 0%, Valor com desconto: 100.00

Digite o valor do produto: 200
Valor original: 200.00, Desconto aplicado: 10%, Valor com desconto: 180.00

Digite o valor do produto: 201
Valor original: 201.00, Desconto aplicado: 20%, Valor com desconto: 160.80

'''