import random

# Opções do jogo
opcoes = ['pedra', 'papel', 'tesoura']

# Placar
placar = {'jogador': 0, 'computador': 0}

while True:
    # O computador escolhe aleatoriamente
    computador = random.choice(opcoes)

    # O jogador escolhe
    jogador = input('Escolha pedra, papel ou tesoura (ou "sair" para encerrar): ')

    # Verifica se o jogador quer sair
    if jogador == 'sair':
        break

    # Verifica se a escolha do jogador é válida
    if jogador not in opcoes:
        continue

    # Mostra a escolha do computador
    print('O computador escolheu:', computador)

    # Compara as escolhas
    if jogador == computador:
        print('Empate!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        print('Você ganhou!')
        placar['jogador'] += 1
    else:
        print('O computador ganhou!')
        placar['computador'] += 1

    # Mostra o placar
    print('Placar: Você -', placar['jogador'], 'Computador -', placar['computador'])

# Mostra o placar final
print('Placar final: Você -', placar['jogador'], 'Computador -', placar['computador'])