from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('951.369.471-28', 'Alfredo', 22)

print('\nPessoa Física')
print(f'Nome: {a.getNome()}')
print(f'CPF: {a.getCPF()}')
print(f'Idade: {a.getIdade()}')

b = PessoaJuridica(CNPJ='83.926.467/6761-04', nome='Empresa X', idade=40)

print('\nPessoa Jurídica:')
print(f'Nome: {b.getNome()}')
print(f'CNPJ: {b.getCNPJ()}')
print(f'Idade: {b.getIdade()}\n')

