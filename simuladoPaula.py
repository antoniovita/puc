pracas = open('pracas.txt' , 'r')
equipes = open('equipes.txt', 'r')

#a)
def criaListaPracas ():
    lista = []
    for linha in pracas:
       elem = linha.strip().split(',')
       lista.append([elem[0], int(elem[1])])
    return lista

#b)
def exibeListaPracas (lista):
    for elem in lista:
        print(f"{elem[0]} {elem[1]}")


#c)
def definePraca(numTotalPracas, nomeEquipe, pratoPrincipal):
    valorBase = 0
    for letra in nomeEquipe:
        if letra in "aeiouAEIOU":
            valorBase +=1
    for letra in pratoPrincipal:
        if letra in "aeiouAEIOU":
            valorBase +=1 
    indice = valorBase % numTotalPracas
    return indice


'''

d] processaEquipes - Recebe a lista de praças. Para cada equipe no arquivo 'equipes.txt', determina a praça correspondente,
exibe o nome da equipe, o prato principal e a praça de destino. Se a praça determinada não tiver mais barracas disponíveis,
o programa deve encontrar outra praça com vaga. Caso não haja mais praças com vagas deve ser exibido "EVENTO LOTADO"
e a função termina.
A cada alocação válida, a quantidade de vagas da praça deve ser decrementada. Essa função deve obrigatoriamente chamar
definePraca.

'''

#d)
def processaEquipes (listaPracas):
    for equipe in equipes:
        info = equipe.strip().split(',')

        idx = definePraca(len(listaPracas), info[0], info[1])

        if listaPracas[idx][1] > 0:
            determinada = listaPracas[idx][0]
            listaPracas[idx][1] -= 1
        else:
            encontrada = False
            for praca in listaPracas:
                if praca[1] > 0:
                    determinada = praca[0]
                    praca[1] -= 1
                    encontrada = True
                    break
            if not encontrada:
                print("EVENTO LOTADO")
                return

        print(f"{info[0]} {info[1]} {determinada}")

#processaEquipes(criaListaPracas())


#2.
#a)
def mudaLista (lista):
    listaFinal = []
    for listinha in lista:
        tipo = listinha[2]
        prato = listinha[1]
        encontrado = False
        for item in listaFinal:
            if item[0] == tipo:
                if prato not in item[1]:
                    item[1].append(prato)
                encontrado = True
                break
        if not encontrado:
            listaFinal.append([tipo, [prato]])
    return listaFinal

'''
#b)
listaNova = mudaLista([
 ["Delicias da Vo Maria", "Torta de Limao", "Sobremesa", 35],
 ["Sabor da Roca", "Feijao Tropeiro", "Regional", 50],
 ["Sabores Urbanos", "Burger de Grao-de-bico", "Vegetariana", 40],
 ["Doces Encantos", "Pudim de Leite", "Sobremesa", 30]
])
for elem in listaNova:
    print(f"Tipo: {elem[0]}")
    for prato in elem[1]:
        print(f"      {prato}")
'''
    
    

'''


Q3) Considere a fórmula fechada para o termo (elemento) an de uma sequência S.
an = 2(n+1) + 3n
, n Є N , n>=1
a) Escreva uma função, denominada geraTermo, que receba um índice n e, usando a fórmula acima, calcule e retorne o
termo (elemento) desse índice.
b) Escreva uma função, exibeTermosAteLimDaSoma, que receba um valor X, e exiba todos os termos da sequência S tais
que a soma não extrapole X.
c) Escreva um bloco principal com 2 testes da função, um com o valor 10000 e um outro escolhido por você (maior do que
10000)
Para o valor 10000, a saída esperada é:
Índice: 1 - Termo: 7
Índice: 2 - Termo: 17
Índice: 3 - Termo: 43
Índice: 4 - Termo: 113
Índice: 5 - Termo: 307
Índice: 6 - Termo: 857
Índice: 7 - Termo: 2443


'''

#3)
#a)
def geraTermo(n):
    termo = 2 * (n + 1) + 3 * n
    return termo

#b)
def exibeTermosAteLimDaSoma(x):
    soma = 0
    i = 1
    while True:
        termo = geraTermo(i)
        if soma + termo > x:
            break
        soma += termo
        print(f"Índice: {i} - Termo: {termo}")
        i += 1

exibeTermosAteLimDaSoma(10000)
print(" ")
exibeTermosAteLimDaSoma(15000)