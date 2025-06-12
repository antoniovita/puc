def contarString (lista): 
    cont = 0
    for elem in lista:
        if isinstance(elem, str):
            cont += 1
    return cont

print(contarString(["oi", 80, True, "oito"]))


def contaCaractere (lista):
    caracteres = 0
    for elem in lista:
        if isinstance(elem, list):
            caracteres += contaCaractere(elem)
        elif isinstance(elem, str):
            caracteres += len(elem)
    return caracteres

print(contaCaractere(["ano", 2016, ["saúde",[2,7.2],'a?'], 'mais 1 email: feliz!']))