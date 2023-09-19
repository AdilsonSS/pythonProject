'''
def hello(meu_nome,idade):
    print('Olá,', meu_nome,'\nSua idade é:',idade)


hello('Adilson',20)
'''

def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

a = calcular_pagamento(200,10)
print(a)
