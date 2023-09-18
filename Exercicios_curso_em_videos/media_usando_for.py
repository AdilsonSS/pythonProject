nota = 0
soma = 0
for i in range(1,5):
    nota = float(input('Digite uma nota:'))
    print(nota)
    soma = soma+nota
media = soma / i
print('A média das 4 notas é {}'.format(media))
