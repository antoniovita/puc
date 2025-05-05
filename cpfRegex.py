import re

# com regex 

def validar_cpf(cpf):
    regex = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if re.match(regex, cpf):
        return True
    return False

#com funcao

def validaCpfComFuncao(cpf):
    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-" or len(cpf) != 14:
        return False
    for i in range(14):
        if i not in [ 3, 7, 11]:
            if not cpf[i].isdigit():
                return False
    return True


cpfValidar = input("Insira um cpf:")
print(validaCpfComFuncao(cpfValidar))