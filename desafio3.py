def desafio3 (num):
    contador = 0
    while (num != 1):
        if (num % 2 == 0):
            num = num/2
            contador +=1
        else:
            num = (num*3) + 1
            contador +=1
    return f"A quantidade de iterações para chegar no número 1 foi de: {contador}"

numero = int(input("Insira um número:"))
print(desafio3(numero))

# 1) Não. Basta testar um número muito grande.
# 2) Não. 17 dá 12 passos e o número 14 dá 17 passos.
# 3) Não. Para n = 3: 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 4) Não, o 9 leva 19 iterações.
# 5) O número 1024 tem 10.

def desafio3item5():
    arrayIteraçõesPorNumero = []
    for num in range(1000, 2000):
        contador = 0
        i = num
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = (i * 3) + 1
            contador += 1
        arrayIteraçõesPorNumero.append((num, contador))
    
    for num, iteracoes in arrayIteraçõesPorNumero:
        if iteracoes < 11:
            print(f"O número {num} levou apenas {iteracoes} iterações para chegar a 1.")
    
print(desafio3item5())
