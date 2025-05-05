import random

def adivinhar ():
    numeroAleatorio = random.randint(1, 1023)


    print("Adivinhe o número que escolhi. Ele está localizado entre 1 e 1023.")
    escolha = int(input("Insira um número:"))


    cont = 0
    while escolha != numeroAleatorio:
        if escolha > numeroAleatorio:
            print("O número é MENOR que esse.")
            cont+=1
            escolha = int(input("Insira um número:"))
        elif escolha < numeroAleatorio:
            print("O número é MAIOR que esse.")
            cont+=1
            escolha = int(input("Insira um número:"))
    print("O número é esse mesmo!")
    print("Parabéns você acertou o número!")    
    print(f"Você levou {cont} tentativas para acertar!")

adivinhar()

