# Função para validar CPF
def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se o CPF não é uma sequência de um único dígito
    for num in range(10):
        if str(cpf) == str(num) * 11:
            return False

    # Calcula os dígitos verificadores do CPF
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (11 - sum(map(calc, enumerate(reversed(cpf[:-2])))) % 11)
    d2 = (11 - sum(map(calc, enumerate(reversed(cpf[:-1])))) % 11)

    # Verifica se os dígitos verificadores calculados são iguais aos informados
    return str(d1 if d1 < 10 else 0) == cpf[-2] and str(d2 if d2 < 10 else 0) == cpf[-1]

# Função para validar CNPJ
def valida_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove caracteres não numéricos

    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Verifica se o CNPJ não é uma sequência de um único dígito
    for num in range(10):
        if str(cnpj) == str(num) * 14:
            return False

    # Calcula os dígitos verificadores do CNPJ
    calc = lambda t: int(t[1]) * ((t[0] % 8) + 2)
    d1 = (11 - sum(map(calc, enumerate(reversed(cnpj[:-2])))) % 11)
    d2 = (11 - sum(map(calc, enumerate(reversed(cnpj[:-1])))) % 11)

    # Verifica se os dígitos verificadores calculados são iguais aos informados
    return str(d1 if d1 < 10 else 0) == cnpj[-2] and str(d2 if d2 < 10 else 0) == cnpj[-1]

# Solicita ao usuário que insira um CPF ou CNPJ
documento = input('Digite o CPF ou CNPJ: ')

# Remove caracteres não numéricos do documento inserido
documento = ''.join(filter(str.isdigit, documento))

# Verifica se o documento inserido é um CPF ou CNPJ e valida-o
if len(documento) == 11:
    print('CPF válido' if valida_cpf(documento) else 'CPF inválido')
elif len(documento) == 14:
    print('CNPJ válido' if valida_cnpj(documento) else 'CNPJ inválido')
else:
    print('Documento inválido')