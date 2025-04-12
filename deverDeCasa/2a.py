def areaExibir (dim1, dim2):
    area = float(dim1)*float(dim2)
    print(f' A área do quadro é: {area}.')
    return area

dim1 = float(input('Insira a primeira dimensão:'))
dim2 = float(input('Insira a segunda dimensão:'))


areaExibir(dim1, dim2)
