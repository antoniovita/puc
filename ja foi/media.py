def passar (n1, n2): 
    media = (n1 + n2)/2
    if ( media >= 5 ):
        resultado = "Passou de ano irmão, só progresso!"
    elif( media < 5 and media >= 3 ):
        if ( n1 > n2 ):
            maiorNota = n1
        else: 
            maiorNota = n2
        notaMinima = 10 - maiorNota
        resultado = f"Prova final lek, jogador resolve no final! Você vai ter que tirar no mínimo {notaMinima}."
    else:
        resultado = "Burro pra caralho, repetiu."
    return resultado


num1 = float(input("Insira a primeira nota:"))
num2 = float(input("Insira a segunda nota:"))

print(passar(num1, num2))
