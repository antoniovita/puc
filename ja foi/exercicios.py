def infoUser ():
    nome = input('Insira seu nome:')
    idade = int(input('Insira sua idade:'))
    altura = float(input('Insira sua altura:'))
    peso = float(input('Insira seu peso:'))
    imc = peso/(altura)**2
    print(f' Nome: {nome}')
    print(f' Idade: {idade}')
    print(f' Altura: {altura:.2f}')
    print(f' Peso: {peso:.1f}')
    print(f' IMC: {imc:.1f}')

infoUser()