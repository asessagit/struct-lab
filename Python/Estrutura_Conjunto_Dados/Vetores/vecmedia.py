# Algoritmo para calcular a media das notas de 60 alunos
n1 = [0] * 60  # Lista para armazenar as notas
n2 = [0] * 60  # Lista para armazenar as notas
soma = 0  # Variável para armazenar a soma das notas
for x in range(60):
    n1[x] = float(input(f"Digite a primeira nota do aluno {x + 1} : "))
    n2[x] = float(input(f"Digite a segunda nota do aluno {x + 1} : "))
    medInd = (n1[x] + n2[x]) / 2  # Calcula a média individual
    soma += medInd  # Acumula a soma das médias individuais
media = soma / 60    # Calcula a média geral
print(f"A média geral das notas é: {media:.2f}")  # Exibe