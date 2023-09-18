# Sorteando os números
import numpy as np
from random import sample, seed

numeros_sorteados = sample(range(1, 61), 6)
numeros_sorteados = sorted(numeros_sorteados)
print(numeros_sorteados)
# lista de aposta ainda vazia
aposta = []

for i in range(1, 7):
    num = 0
    while num < 1 or num > 60 or num in aposta:
        num = int(input(f'{i}º número - Digite um número entre 1 e 60 '))
        
            
    aposta.append(num)

aposta = sorted(aposta)
print('\nSua aposta: ', aposta)

# Conferindo resultados e acertos
resultado = np.in1d(aposta, numeros_sorteados)
acertos = len(np.intersect1d(aposta, numeros_sorteados))

# Resultados
print('#' * 11, 'Você ganhou na Mega Sena!', '#' * 11) if resultado.all() else print(
    f'Você perdeu e acertou {acertos} número(s).')
print('\nSorteio:   ', numeros_sorteados)
print('Sua aposta:  ', aposta)
