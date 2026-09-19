from random import randint
# Importa apenas a função randint da biblioteca random.
# Ela será usada para gerar um número inteiro aleatório dentro de um intervalo.

print('#### Iniciando Jogo ####')
# Exibe uma mensagem inicial para indicar que o jogo começou.

target, chances = randint(0, 100), 10
# Gera um número aleatório entre 0 e 100 e guarda em 'target'.
# Define também o número de chances que o jogador terá (10).

for c in range(chances, 0, -1):
    # Cria um loop que vai de 'chances' até 1, decrementando de 1 em 1.
    # Isso controla quantas tentativas restam.

    val = input(f'Tentativa {11-c}/10. Chute (0-100): ')
    # Pede ao jogador para digitar um número.
    # A mensagem mostra qual tentativa está sendo feita.
    # O f-string permite inserir variáveis diretamente na string.
    # O /10 é apenas texto dentro da f-string, não uma divisão. Ele aparece para indicar que são 10 tentativas no total.
    # 

    if not val.isnumeric():
        print('Por favor, digite apenas números!\n')
        continue
    # Verifica se o valor digitado é numérico.
    # Se não for, mostra aviso e volta para o início do loop sem gastar a chance.

    chute = int(val)
    # Converte o valor digitado para inteiro.

    if chute == target:
        print(f'\nParabéns! Você venceu. O número era {target} e restaram {c-1} chances.\n')
        break
    # Se o chute for igual ao número sorteado, mostra mensagem de vitória
    # e interrompe o loop com 'break'.

    print(f"Errou! Dica: O número secreto é {'menor' if chute > target else 'maior'}.\n")
    # Se o chute não for igual, mostra mensagem de erro.
    # Usa operador ternário para dar uma dica:
    # - Se o chute foi maior que o número, diz que o número secreto é menor.
    # - Caso contrário, diz que é maior.

else:
    print(f'\nSuas chances acabaram, você perdeu! O número era {target}.\n')
# O bloco 'else' do 'for' só é executado se o loop terminar sem 'break'.
# Ou seja, se o jogador não acertar em nenhuma tentativa, mostra mensagem de derrota.

print('#### Fim do Jogo ####')
# Exibe mensagem final indicando que o jogo terminou.



