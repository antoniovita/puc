def mdc(numMaior, numMenor):
    MaiorDivisor = 1
    arrayDivisores = []
    i = 1
    while i <= numMenor:
        if numMaior % i == 0 and numMenor % i == 0: 
            arrayDivisores.append(i)
            MaiorDivisor = i
        i += 1
    return MaiorDivisor, arrayDivisores


maior = int(input("Insira o maior número: "))
menor = int(input("Insira o menor número: "))

print(mdc(maior, menor))