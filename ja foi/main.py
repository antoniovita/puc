'''def funcao(num1,num2):
    return num1 + num2
resultado = funcao(3,4)
print(resultado)

def printarAteNumero(num):
    i = 1
    while i <= num:
        print(i)
        i += 1

printarAteNumero(20)'''


# 1) area do triangulo escaleno
'''
import math

def areaEscaleno (lado1, lado2, angulo):
    area = (lado1 * lado2 * math.sin(math.radians(angulo)) )/2
    return area

areaDoTrianguloEscaleno = areaEscaleno(10,8,60)

print(areaDoTrianguloEscaleno)'''

# equacao de segundo grau 
'''
def equacao2grau(a, b, c):
    delta = (b**2 - 4*a*c)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    resposta = "O x1 é " + str(x1) + " e o x2 é " + str(x2)
    return resposta

resultado = equacao2grau(2,6,-20)
print(resultado)
'''
'''
import random

def escolherLetra ():
    letras = 'abcdefghijklmnopqrstuvwxyz'
    return random.choice(letras)
resultado = escolherLetra()
print(resultado)

def nomeAsterisco():
    nome = input('Qual o seu nome? ')
    tamanho = len(nome)
    asteriscos = '*' * (tamanho // 2)
    stringeAst = f"{asteriscos}{nome}{asteriscos}"
    print(stringeAst)

nomeAsterisco()

def pesar():
    pesoTotal = 2578 + 172
    kg = round(pesoTotal // 1000)
    g = pesoTotal % 1000
    resposta = f' O peso é de {kg} kg e {g} gramas'
    return resposta

resultado2 = pesar()
print(resultado2)

'''

'''
Var Nota1, Nota2, NotaFinal float
Ler Nota1
Ler Nota2
NotaFinal = (Nota1 + Nota2)/2.0
Imprimir NotaFinal

'''
'''
def media ():
    nota1 = float(input('Insira a primeira nota:'))
    nota2 = float(input('Insira a segunda nota:'))
    notafinal = (nota1 + nota2)/2

    if(notafinal >= 5):
        condicao = 'aprovado'
    else: 
        condicao = 'reprovado'

    resposta = f'O aluno teve como média: {notafinal} e foi {condicao}'
    return resposta

resultado = media()
print(resultado)
'''


'''

#m = vp + (vp * i / 100 * t) + vf * te


def motante ():
    vp = float(input('Insira o valor da prestação:'))
    t = float(input('Insira o tempo em dias de atraso do pagamento:'))
    i = float(input('Insira a taxa de juros: '))
    if ( t < 10 ): 
        montanteNormal = vp + (vp * i / 100 * t)
        resultado = montanteNormal
    else: 
        vf = float(input('Insira o valor fixo:'))
        montanteFinal = montanteNormal + (vf * (t-10))
        resultado = montanteFinal
    return resultado

print(motante())

'''
'''
def alturaArvore (hInicial, taxa, n):
    alturaFinal = (hInicial + hInicial*(taxa)**n)
    return alturaFinal

print(alturaArvore(4, 1.2, 5))
'''

'''
def calculoPDobrar(valor, taxa):
    anos = 0
    saldo = valor
    while saldo < 2 * valor:
        saldo *= (1 + taxa)
        anos += 1
    return anos

valor_inicial = float(input("Informe o valor inicial: "))
taxa_juros = float(input("Informe a taxa de juros anual (ex: 0.1 para 10%): "))
print(f"Serão necessários {calculoPDobrar(valor_inicial, taxa_juros)} anos para duplicar o valor inicial.")'
'''
'''
def perguntarIdade():
    idades = []
    menores = []
    maisde20 = []
    i = 0
    while i < 6:
        idade = int(input("Digite a idade da pessoa: "))
        idades.append(idade)
        if idade < 18:
            menores.append(idade)
        elif idade > 20:
            maisde20.append(idade)
        i += 1

    idadeMaisvelha = max(idades)
    media = sum(idades) / len(idades)
    percentualMaisde20 = (len(maisde20) / len(idades)) * 100 

    resultado = f'A quantidade de pessoas menores de idade é {len(menores)} a média delas é {media} a pessoa mais velha tem {idadeMaisvelha} e o percentual de pessoas maiores de 20 é {percentualMaisde20}%'
    print(resultado)

perguntarIdade()
'''

def perguntarNome ():
    nome = input('Insira seu nome:')
    print ( f' Seu nome é {nome}')
perguntarNome()