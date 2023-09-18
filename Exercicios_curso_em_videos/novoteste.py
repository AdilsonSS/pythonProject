import requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen
pesquisa_cep = input('digite o cep')
if len(pesquisa_cep) != 8:
    print('cep inválido')


request = requests.get('https://viacep.com.br/ws{}/joson/'.format(pesquisa_cep))
print(request.json())
endereco = request.json()
print('Logradouro: {}'.format(endereco[logradouro]))

