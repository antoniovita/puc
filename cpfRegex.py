def validaCpfComFuncao(cpf):
    if len(cpf) != 14 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False

    cpf_numeros = [int(c) for i, c in enumerate(cpf) if i not in [3, 7, 11]]

    if len(cpf_numeros) != 11:
        return False

    if cpf_numeros == cpf_numeros[::-1] and cpf_numeros.count(cpf_numeros[0]) == 11:
        return False

    soma1 = sum([cpf_numeros[i] * (10 - i) for i in range(9)])
    digito1 = 0 if (soma1 * 10 % 11) >= 10 else (soma1 * 10 % 11)

    soma2 = sum([cpf_numeros[i] * (11 - i) for i in range(10)])
    digito2 = 0 if (soma2 * 10 % 11) >= 10 else (soma2 * 10 % 11)

    return cpf_numeros[9] == digito1 and cpf_numeros[10] == digito2

cpfValidar = input("Insira um CPF: ")
if validaCpfComFuncao(cpfValidar):
    print("CPF válido.")
else:
    print("CPF inválido.")
