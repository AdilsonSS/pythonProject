#https://www.youtube.com/watch?v=m72WIejruxI&t=64s

import requests
cep = "26195710"
link = f'https://viacep.com.br/ws/{cep}/json/'
requisicao = requests.get(link)
print(requisicao)
#print(requisicao.json())
#
dic_requisicao = requisicao.json()
uf = dic_requisicao['uf']
cidade = dic_requisicao['localidade']
bairro = dic_requisicao['bairro']
logradouro = dic_requisicao['logradouro'] 
print('UF:',uf, '\nCidade:', cidade, '\nBairro:', bairro, '\nEndereço:',logradouro)

''' Outra forma de fazer a requisição:
print(requisicao.json()['uf'])
'''