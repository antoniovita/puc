l1 = [3,7,1,90,2]
l2 = [3,[98,2,1],10]

def exibe(lista):
    for elemento in lista:
        print(elemento)
    return

exibe(l1)
exibe(l2)

def somar(lista):
    cont = 0 
    for element in lista:
        if isinstance(element, int):
            cont += element
        elif isinstance(element, list):
            cont += sum(element)
    return cont 

print(somar(l2))
print(somar(l1))