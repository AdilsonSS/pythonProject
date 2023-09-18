import datetime
nome = (input('digite seu nome'))
print('É um Prazer te conhecer, {}!'.format(nome))
#print(f'É um Prazer te conhecer, {nome}!')

def parse_expenses(expenses_string):
    '''Parse list of expenses and return the list of triples (date, value, curremcy)'''
    