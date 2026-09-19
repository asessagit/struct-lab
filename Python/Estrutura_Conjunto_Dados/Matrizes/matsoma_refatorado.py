# Algoritmo para calcular a soma de uma matriz de dimensão 4x2

# Função para ler um número real com validação
def ler_float(mensagem):
    while True:
        valor = input(mensagem).strip()
        # Troca vírgula por ponto, se houver
        valor = valor.replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Entrada inválida! Digite apenas números reais (ex: 115.6).")

# Algoritmo para calcular a soma de uma matriz de dimensão 4x2
num = [[ler_float(f"Digite o elemento MA[{i+1},{j+1}]: ") for j in range(2)] for i in range(4)]

# Calcula a soma
soma = sum(elem for linha in num for elem in linha)

# Exibe a soma
print(f"\nA soma dos elementos da matriz é: {soma:.2f}")

# Exibe a matriz com linhas de grade
print("\nMatriz digitada:")
colunas = len(num[0])
largura = 10  # largura fixa para cada célula

def linha_horizontal():
    print("+" + "+".join("-" * largura for _ in range(colunas)) + "+")

linha_horizontal()
for linha in num:
    print("|" + "|".join(f"{elem:^{largura}.2f}" for elem in linha) + "|")
    linha_horizontal()


'''
Aceita vírgula ou ponto como separador decimal.

Se o usuário digitar letras ou símbolos inválidos, mostra mensagem e pede novamente.

List comprehension → preenche a matriz direto, sem inicializar com zeros.

sum() com flatten → soma todos os elementos em uma linha elegante.

Formatação :.2f → mostra os números com duas casas decimais.

join → imprime cada linha da matriz alinhada, como uma tabela.

Título “Matriz digitada” → deixa claro que é a matriz original.

{elem:8.2f} → formata cada número com 2 casas decimais e largura fixa de 8 caracteres.

Isso garante que os números fiquem alinhados em colunas, mesmo que tenham tamanhos diferentes.

A matriz agora aparece como uma tabela bem organizada.

Função auxiliar linha_horizontal() para desenhar as bordas.

join para repetir os traços - em cada coluna.

Agora cada linha da matriz fica delimitada por bordas horizontais e verticais, formando uma tabela clara.

Exemplo de saída: 
Digite o elemento MA[1,1]: 1
Digite o elemento MA[1,2]: 2
Digite o elemento MA[2,1]: 3,1
Digite o elemento MA[2,2]: 4,2
A soma dos elementos da matriz é: 10.30
Matriz digitada:
+----------+----------+
|   1.00   |   2.00   |
+----------+----------+
|   3.10   |   4.20   |
+----------+----------+



'''
