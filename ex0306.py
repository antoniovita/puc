def geraListaDisciplinasSet (lista):
    resposta = set()
    for elem in lista:
        if elem[2] >= 8:
            resposta.add(elem[0])
    return resposta

'''print(geraListaDisciplinasSet(
[['INF2020', 'Kadinho', 5.2],
['MAT1010', 'Maya', 8.5],
['CTC4002', 'Ana', 10.0],
['FIS1312', 'Maria', 7.9],
['INF2020', 'Maria', 9.2],
['ENG1381', 'Marcos', 6.3],
['INF2020', 'Ana', 8.2],
['FIS1312', 'Carla', 4.9],
['MAT1010', 'José', 3.5],
['CTC4002', 'João', 6.9],
['MAT1010', 'Raquel', 9.9],
['ENG1381', 'Kadinho', 7.7]])
)'''


def geraListaDisciplinas (lista):
    resposta = []
    for elem in lista:
        if elem[2] >= 8:
            if elem[0] not in resposta:
                resposta.append(elem[0])
    return resposta

print(geraListaDisciplinas(
[['INF2020', 'Kadinho', 5.2],
['MAT1010', 'Maya', 8.5],
['CTC4002', 'Ana', 10.0],
['FIS1312', 'Maria', 7.9],
['INF2020', 'Maria', 9.2],
['ENG1381', 'Marcos', 6.3],
['INF2020', 'Ana', 8.2],
['FIS1312', 'Carla', 4.9],
['MAT1010', 'José', 3.5],
['CTC4002', 'João', 6.9],
['MAT1010', 'Raquel', 9.9],
['ENG1381', 'Kadinho', 7.7]])
)