def sequencia(n):
    # Verifica se n é igual a 1, que é o caso base da recursão
    if n == 1:
        # Define o primeiro valor da sequência como 2
        R = 2
        # Exibe o valor calculado
        print(R)
        # Retorna o resultado da sequência
        return R
    else:
        # Chama a função novamente com n reduzido em 1
        # e multiplica o resultado por 2
        R = 2 * sequencia(n - 1)
        # Exibe o valor calculado
        print(R)
        # Retorna o resultado da sequência
        return R
# Main Program
# Executa a função com o valor inicial 
resultado = sequencia(10)

# Exibe o resultado final retornado pela função
print(f"O resultado final da função recursiva é: ",{resultado})
