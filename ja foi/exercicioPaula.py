#1) 

lista = [ 'Daniel', 'Livia', 'Daniela']
def exibir ():
    num = int(input(f' Insira um número de 0 até {len(lista)}:'))
    print(lista[num])

exibir()

#2)

def balas():
    crianca = int(input('Insira a quantidade de crianças:'))
    balas = int(input('Insira a quantidade de balas:'))
    balasporcrianca = balas/crianca
    print(f' A quantidade de balas por criança será de {balasporcrianca:.0f}.')
balas()
