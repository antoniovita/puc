def contarAlgarismos(n):
    if n < 10:
        return 1
    else:
        return 1 + contarAlgarismos(n // 10)

print(contarAlgarismos(123456))
