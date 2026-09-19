# Algoritmo para calcular a diferença entre o estoque atual e o estoque anterior de 5 produtos
EstAnt = [0] * 5  # Lista para armazenar o estoque anterior
EstAtu = [0] * 5  # Lista para armazenar o estoque atual
saida = [0] * 5   # Lista para armazenar a diferença entre os estoques

for i in range(5):
    EstAnt[i] = int(input(f"Digite o estoque anterior do produto {i + 1}: "))
    EstAtu[i] = int(input(f"Digite o estoque atual do produto {i + 1}: "))

for i in range(5):
    saida[i] = EstAtu[i] - EstAnt[i]  # Calcula a diferença
    
    if saida[i] < 0:
        print(f"Saíram {-saida[i]} unidades do produto {i + 1}")
    elif saida[i] > 0:
        print(f"Entraram {saida[i]} unidades do produto {i + 1}")
    else:
        print(f"O estoque do produto {i + 1} não mudou")
