def contarAlg(algRecebido, num):
    if num < 10:
        if num == algRecebido:
            return 1 
        else: 
            return 0
    else:
        ultimoDigito = num % 10
        if ultimoDigito == algRecebido:
            cont = 1 
        else:
            cont = 0
        return cont + contarAlg(algRecebido, num // 10)

print(contarAlg(2, 12342))