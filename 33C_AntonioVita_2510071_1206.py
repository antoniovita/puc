p1 = open("p1.txt", "r")
t1 = open("t1.txt", "r")
preocupacoesArq = open("preocupacoes.txt", "w")
notasArq = open("notas.txt", "w")


def mediaAlunos(prova, teste, preocupacoes, notas):
    prova_linhas = prova.readlines()
    teste_linhas = teste.readlines()

    alunos = []
    notaProva = []
    notaTeste = []

    for linha in prova_linhas:
        partes = linha.strip().split()
        alunos.append(partes[0])
        notaProva.append(float(partes[1]))

    for linha in teste_linhas:
        partes = linha.strip().split()
        notaTeste.append(float(partes[1]))

    for i in range(len(alunos)):
        media = notaProva[i] * 0.8 + notaTeste[i] * 0.2
        if notaProva[i] < 4:
            preocupacoes.write(f"{alunos[i]} {media:.2f}\n")
        if notaTeste[i] > 7:
            notas.write(f"{alunos[i]} {media:.2f}\n")

mediaAlunos(p1, t1, preocupacoesArq, notasArq)

p1.close()
t1.close()
preocupacoesArq.close()
notasArq.close()
