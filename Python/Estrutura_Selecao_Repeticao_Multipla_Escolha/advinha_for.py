from random import randint

print('#### Iniciando Jogo ####')
random_num = randint(0, 100)
chances_maximas = 10

# range(10, 0, -1) gera a sequência: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
for chances_restantes in range(chances_maximas, 0, -1):
    chute = input(f'Chute um número entre 0 e 100 (Tentativas restantes: {chances_restantes}): ')
    
    if chute.isnumeric():
        chute = int(chute)
    else:
        print('Entrada inválida! Digite apenas números inteiros.\n')
        continue
        
    if chute == random_num:
        print(f'\nParabéns, você venceu! O número era {random_num} e você ainda tinha {chances_restantes - 1} chances.\n')
        break
    else:
        print('')
        if chute > random_num:
            print('Você errou!!! Dica: É um número menor.')
        else:
            print('Você errou!!! Dica: É um número maior.')
        print(f'Você ainda possui {chances_restantes - 1} chances.\n')
else:
    # Bloco executado caso o loop for complete todas as iterações sem break
    print(f'\nSuas chances acabaram, você perdeu! O número secreto era {random_num}.\n')

print('#### Fim do Jogo ####')
