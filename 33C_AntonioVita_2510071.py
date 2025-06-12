arquivo1 = open('arquivoBase.txt', 'r')
arquivo2 = open('arquivoFinal.txt', 'w')

coringaOpcao = int(input("Insira o coringa:"))


def numeroCoringa (arquivoBase, arquivoFinal, coringa):
    for num in arquivoBase:
        if int(num) % coringa == 0:
            arquivoFinal.write(num)

numeroCoringa(arquivo1, arquivo2, coringaOpcao)

            
