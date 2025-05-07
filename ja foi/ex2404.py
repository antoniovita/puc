def perguntarIdade (n):
    arrayIdades = []
    menores = 0
    mais30 = 0
    for i in range(n):
        idade = int(input("Insira a idade:"))
        arrayIdades.append(idade)
        if (idade < 18):
            menores += 1
        elif (idade > 30):
            mais30 += 1

    totalIdades = sum(arrayIdades)
    media = totalIdades/len(arrayIdades)

    percentualmenores = (menores/len(arrayIdades))*100
    percentualmais30 = (mais30/len(arrayIdades))*100

    print(f' A média de idades: é {media}')
    print(f' O percentual de menores é de {percentualmenores}%.')
    print(f' O percentual de maiores de 30 anos é {percentualmais30}%.')

numero = int(input("Insira o número de pessoas:"))
perguntarIdade(numero)