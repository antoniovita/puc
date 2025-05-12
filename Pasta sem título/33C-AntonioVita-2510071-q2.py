def contem2(num):
    if num == 0:
        return False
    ultimoDigito = num % 10
    if ultimoDigito == 2:
        return True
    else:
        return contem2(num // 10)


print(contem2(21312))
