# Calculando desconto de um produto

prod = float(input('Qual o preço do produto? '))
desc = prod * 5 / 100
print('com desconto de 5%, o valor é R$ {}'.format(prod - desc))
