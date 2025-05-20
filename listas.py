import random

lgrande = random.sample(range(-20, 20), 14)
print(lgrande)

def retornaProduto (lista):
    num = lista[0]
    for i in range (1, len(lista) - 1):
        num *=lista[i]
    return num

#print(retornaProduto(lgrande))

def retornaMedia(lista):
    return sum(lista)/len(lista)

#print(retornaMedia(lgrande))

def retornaMaiorValor(lista):
    return max(lista)

#print(retornaMaiorValor(lgrande))

def trocaPorQuatro (lista):
    for i in range(len(lista)):
        if lista[i] % 4 == 0:
            lista[i] = 0
    return lista

#print(trocaPorQuatro(lgrande))

