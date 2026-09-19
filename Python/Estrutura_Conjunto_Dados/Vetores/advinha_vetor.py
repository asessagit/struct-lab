from random import randint

print('#### Iniciando Jogo Otimizado ####')
target = randint(0, 100)
chances = 10
historico_chutes = [] # Vetor que armazena os palpites (Conceito da Unidade 3)

for tentativa in range(1, chances + 1):
    val = input(f'Tentativa {tentativa}/{chances}. Digite seu chute (0-100): ')
    
    # Correção do Bug 2 (TypeError) por validação robusta
    if not val.isnumeric():
        print('Erro! Digite um número inteiro válido. Tente novamente.\n')
        continue
    
    chute = int(val)
    
    # Verificação inteligente de duplicidade usando o histórico de chutes (Vetor)
    if chute in historico_chutes:
        print(f'Atenção! Você já chutou o número {chute} antes. Seu histórico: {historico_chutes}')
        print('Tente outro número para não gastar suas tentativas!\n')
        continue
        
    # Adicionando o elemento de forma dinâmica ao vetor na memória
    historico_chutes.append(chute)
    
    if chute == target:
        print(f'\n🎉 PARABÉNS! Você acertou na tentativa {tentativa}!')
        print(f'O número era {target}. Histórico de palpites: {historico_chutes}\n')
        break
    
    dica = 'MENOR' if chute > target else 'MAIOR'
    print(f'Você errou! Dica: O número secreto é {dica} que {chute}.')
    print(f'Histórico atual de palpites realizados: {historico_chutes}\n')
else:
    print(f'\n😢 Suas chances acabaram! O número secreto era {target}.')
    print(f'Seu histórico final de tentativas: {historico_chutes}\n')

print('#### Fim do Jogo ####')
