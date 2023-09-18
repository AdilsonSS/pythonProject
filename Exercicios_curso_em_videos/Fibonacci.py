#sequencia de fibonacci

n = int(input('Quantos termos para mostrar? '))
if n == 0:
    print('vc digitou 0')
    exit()
if n == 1:
    print (0)
    exit()

t1 = 0
t2 = 1
print('~' * 30)
print('{} → {}'.format(t1, t2), end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
