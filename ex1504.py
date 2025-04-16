def litros(quantidade):
    lista = []
    for i in range(1, quantidade + 1):
        peso = float(input(f'Peso do aluno {i}: '))
        lista.append(peso)

    for idx, peso in enumerate(lista, start=1):
        litros = (35 * peso / 1000)
        print(f'Aluno {idx} - Peso: {peso} - Litros de água: {litros:.2f}')

    i = 0
    contador = 0
    while (i < len(lista)):
        if ((lista[i]) * 35 / 1000 > 2):
            contador += 1
        i += 1
    
    total = sum((35 * peso / 1000) for peso in lista)
    print(f' Total de litros consumidos pela turma: {total:.2f}')

    print(f' Média da turma: {total/len(lista)}')
    print(f'Quantidade de alunos que bebem mais de 2L: {contador}')
    
def turmas ():
    numero = int(input('Insira a quantidade de turmas:'))

    for i in range(numero):
        quantidadeTurma = int(input('Insira a quantidade de alunos da turma:'))
        print(f'Turma {i +1}:')
        litros(numero)

turmas()