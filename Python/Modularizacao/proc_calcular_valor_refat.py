# Função para ler um número real ou inteiro com validação
def ler_numero(mensagem):
    while True:  # loop infinito até o usuário digitar corretamente
        valor = input(mensagem).strip()  # lê a entrada e remove espaços extras
        valor = valor.replace(",", ".")  # aceita vírgula como separador decimal
        try:
            numero = float(valor)  # tenta converter para float (aceita int e real)
            return numero
        except ValueError:  # se não conseguir converter (entrada inválida)
            print("Erro: digite apenas números inteiros ou reais (ex: 10 ou 115.6).")
            # mostra mensagem de erro e volta ao início do loop

# Procedimento para calcular o valor com desconto baseado em faixas de preço
def calcular_desconto(valor):
    # Usa expressão condicional (ternária) para simplificar a lógica
    desconto = 0 if valor <= 100 else 0.1 if valor <= 200 else 0.2
    # até 100 → 0%, até 200 → 10%, acima de 200 → 20%
    
    valor_final = valor * (1 - desconto)  # cálculo direto do valor com desconto
    
    # Exibe os resultados formatados
    print(f"Valor original: {valor:.2f}, "
          f"Desconto aplicado: {desconto*100:.0f}%, "
          f"Valor com desconto: {valor_final:.2f}")

# Main program
valor = ler_numero("Digite o valor do produto: ")  # entrada validada
calcular_desconto(valor)  # chamada da função

'''
Exemplo de entrada e saída:

Digite o valor do produto: 100
Valor original: 100.00, Desconto aplicado: 0%, Valor com desconto: 100.00

Digite o valor do produto: 200
Valor original: 200.00, Desconto aplicado: 10%, Valor com desconto: 180.00

Digite o valor do produto: 201,50
Valor original: 201.50, Desconto aplicado: 20%, Valor com desconto: 161.20

1. Função ler_numero para validar a entrada.

2. Aceita int (10) e float (115.6 ou 12,5).

3. Qualquer caractere inválido gera mensagem de erro e pede novamente.

4. A lógica de desconto foi simplificada com operador ternário.

'''