# Define a função recursiva da Torre de Hanói.
def torre_hanoi(n, origem, destino, auxiliar, movimento=1):
    # Verifica se resta apenas um disco para mover.
    if n == 1:
        # Exibe o número do movimento e as torres envolvidas.
        print(f"{movimento}. Mova o disco de {origem} para {destino}")
        # Retorna o número do próximo movimento.
        return movimento + 1

    # Move os discos superiores para a torre auxiliar.
    movimento = torre_hanoi(
        n - 1, origem, auxiliar, destino, movimento
    )

    # Move o maior disco da origem para o destino.
    print(f"{movimento}. Mova o disco de {origem} para {destino}")

    # Incrementa o contador de movimentos.
    movimento += 1

    # Move os discos da torre auxiliar para o destino.
    return torre_hanoi(
        n - 1, auxiliar, destino, origem, movimento
    )


# Solicita ao usuário a quantidade de discos.
num_discos = int(input("Digite o número de discos: "))

# Inicia a movimentação da torre A para a torre C,
# utilizando a torre B como auxiliar.
torre_hanoi(num_discos, "A", "C", "B")


'''
Curiosidade: 

O inventor do jogo Torre de Hanói foi o matemático francês Édouard Lucas (1842-1891).

“No começo dos tempos, Deus criou a Torre de Brahma, que contém três hastes de diamante, e colocou na primeira
haste 64 discos de ouro maciço. Deus chamou seus sacerdotes e ordenou-lhes que transferissem todos os discos 
para a terceira haste, seguindo as regras acima descritas. Os sacerdotes, então, obedeceram e começaram o 
trabalho de remoção dos discos, dia e noite. Segundo Deus, quando eles terminarem o trabalho, 
a Torre de Brahma irá ruir e o mundo acabará…”

Para 64 discos, o número mínimo de movimentos é:

[2^{64} - 1 = 18.446.744.073.709.551.615]

Portanto, seriam necessários 18.446.744.073.709.551.615 movimentos.


Confira em: https://clubes.obmep.org.br/blog/torre-de-hanoi/ 

Exemplo de entrada e saída da função recursiva para 6 discos

Número mínimo de movimentos para 6 discos é: [2^6 - 1 = 63]
Digite o número de discos: 6
1. Mova o disco de A para B
2. Mova o disco de A para C
3. Mova o disco de B para C
4. Mova o disco de A para B
5. Mova o disco de C para A
6. Mova o disco de C para B
7. Mova o disco de A para B
8. Mova o disco de A para C
9. Mova o disco de B para C
10. Mova o disco de B para A
11. Mova o disco de C para A
12. Mova o disco de B para C
13. Mova o disco de A para B
14. Mova o disco de A para C
15. Mova o disco de B para C
16. Mova o disco de A para B
17. Mova o disco de C para A
18. Mova o disco de C para B
19. Mova o disco de A para B
20. Mova o disco de C para A
21. Mova o disco de B para C
22. Mova o disco de B para A
23. Mova o disco de C para A
24. Mova o disco de C para B
25. Mova o disco de A para B
26. Mova o disco de A para C
27. Mova o disco de B para C
28. Mova o disco de A para B
29. Mova o disco de C para A
30. Mova o disco de C para B
31. Mova o disco de A para B
32. Mova o disco de A para C
33. Mova o disco de B para C
34. Mova o disco de B para A
35. Mova o disco de C para A
36. Mova o disco de B para C
37. Mova o disco de A para B
38. Mova o disco de A para C
39. Mova o disco de B para C
40. Mova o disco de B para A
41. Mova o disco de C para A
42. Mova o disco de C para B
43. Mova o disco de A para B
44. Mova o disco de C para A
45. Mova o disco de B para C
46. Mova o disco de B para A
47. Mova o disco de C para A
48. Mova o disco de B para C
49. Mova o disco de A para B
50. Mova o disco de A para C
51. Mova o disco de B para C
52. Mova o disco de A para B
53. Mova o disco de C para A
54. Mova o disco de C para B
55. Mova o disco de A para B
56. Mova o disco de A para C
57. Mova o disco de B para C
58. Mova o disco de B para A
59. Mova o disco de C para A
60. Mova o disco de B para C
61. Mova o disco de A para B
62. Mova o disco de A para C
63. Mova o disco de B para C
'''