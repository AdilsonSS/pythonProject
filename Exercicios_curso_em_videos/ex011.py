# Medida para pintar parede

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = a * l
print('Parede com dimensão {} X {}.\nA area é de {} m²'.format(a,l,area))
tinta = area / 2
print('Para pintar a parede será necessário {} litros de tinta'.format(tinta))
