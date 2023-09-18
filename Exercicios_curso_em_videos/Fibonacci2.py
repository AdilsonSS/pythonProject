#sequencia de fibonacci
import emoji

print('SEQUENCIA DE FIBONACCI')
print('#'*30)
n = int(input('Qual a quantidade de sequência? '))
while n == 0:
    print('vc digitou 0. Digite um número valido')
    n = int(input('Qual a quantidade de sequência? '))

t1 = 0
t2 = 1

for i in range(n):
    t3 = t1 + t2
    print('{} → '.format(t1), end='')
    t1 = t2
    t2 = t3
print('FIM')

'''
t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end = '')
cont = 3
while cont <= n:
    t3 = t1 +t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

'''