#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

# Importa o módulo para trabalhar com raízes reais e complexas
import cmath as mat


# Exibe uma mensagem inicial
print("Ambiente Python pronto no WSL2 UBUNTU 24.04/.devcontainer ")


# Recebe os coeficientes da equação
a = float(input("Digite um número para a: "))
# Continua solicitando enquanto a for igual a zero
while a == 0:
    print("O valor de a não pode ser 0.")
    a = float(input("Digite outro valor para a: "))
# Recebe os outros coeficientes somente após a ser válido
b = float(input("Digite um número para b: "))
c = float(input("Digite um número para c: "))


# Calcula o discriminante da equação
D = b**2 - 4 * a * c


# Informa quando as raízes não são reais
if D < 0:
    print("A equação não possui raízes reais.")
    print("Calculando as raízes complexas...")


# Calcula as duas raízes da equação
x1 = (-b + mat.sqrt(D)) / (2 * a)
x2 = (-b - mat.sqrt(D)) / (2 * a)


# Exibe a raiz arredondada corretamente
def mostrar_raiz(nome, raiz):
    # Arredonda a parte real e a parte imaginária
    parte_real = round(raiz.real, 2)
    parte_imaginaria = round(raiz.imag, 2)

    # Exibe somente a parte real quando não existe parte imaginária
    if parte_imaginaria == 0:
        print(f"{nome} = {parte_real}")

    # Exibe a raiz complexa com sinal e duas casas decimais
    else:
        sinal = "+" if parte_imaginaria > 0 else "-"
        print(
            f"{nome} = {parte_real} "
            f"{sinal} {abs(parte_imaginaria)}j"
        )


# Mostra os resultados finais
mostrar_raiz("x1", x1)
mostrar_raiz("x2", x2)