#Carro alugado calcular preço a pagar
dias = int(input('Quantos dias de aluguel do carro? '))
km = float(input('Quantos km percorrido? '))
valor = (60 * dias) + (0.15 * km)
print(f'O valor a ser pago é R$ {valor:.2f}')
