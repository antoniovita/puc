from getpass import getpass

def forca (palavra):

    arrayDasLetras = list(palavra)
    tentativas = len(palavra)

    oculto = []
    for i in range(tentativas):
        oculto.append("_")
    print(' '.join(oculto))


    while tentativas > 0 and "_" in oculto:
        letra = input("Insira uma letra:")
        acertou = False

        for idx, char in enumerate(arrayDasLetras):
            if (letra == char):
                oculto[idx] = letra
                acertou = True
                
        if acertou == True:
            print("Acertou!")
            
        else:
            print("Errou!")

        tentativas -=1
        print(' '.join(oculto))
        print(f"Tentativas restantes: {tentativas}")
    
    if "_" not in oculto: 
        print("Parabéns, você acertou!")
    else:
        print(f"Você perdeu, a palavra era {palavra}")

print("Bem vindo ao jogo da forca")
palavra = getpass("Insira a palavra secreta:")
forca(palavra)
