from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('111.222.333-44', 'Alfredo', 22)

print('\nPessoa Física')
print(f'Nome: {a.getNome()}')
print(f'CPF: {a.getCPF()}')
print(f'Idade: {a.getIdade()}')

b = PessoaJuridica(CNPJ='64.614.527/0001-99', nome='Empresa X', idade=40)

print('\nPessoa Jurídica:')
print(f'Nome: {b.getNome()}')
print(f'CNPJ: {b.getCNPJ()}')
print(f'Idade: {b.getIdade()}\n')
