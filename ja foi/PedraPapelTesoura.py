import random

def jogo (escolha):
    arrayEscolhas = ["PEDRA", "PAPEL", "TESOURA"]
    numeroAleatorio = random.randint(0, 2)
    escolhaDoPc = arrayEscolhas[numeroAleatorio]

    if escolha == 1:
        opcao = "PEDRA"
        print(f"Você escolheu: {opcao}")
    elif escolha == 2: 
        opcao = "PAPEL"
        print(f"Você escolheu: {opcao}")
    elif escolha == 3:
        opcao = "TESOURA"
        print(f"Você escolheu: {opcao}")
    else:
        print("Escolha não válida.")
        return

    print(f'O Computador escolheu: {escolhaDoPc}')

    if opcao == "PEDRA" and escolhaDoPc == "PAPEL":
        print("Você perdeu.")
    elif opcao == "PEDRA" and escolhaDoPc == "TESOURA":
        print("Você ganhou.")
    if opcao == "PEDRA" and escolhaDoPc == "PEDRA":
        print("Você empatou.")

    if opcao == "PAPEL" and escolhaDoPc == "TESOURA":
        print("Você perdeu.")
    elif opcao == "PAPEL" and escolhaDoPc == "PEDRA":
        print("Você ganhou.")
    if opcao == "PAPEL" and escolhaDoPc == "PAPEL":
        print("Você empatou.")


    if opcao == "TESOURA" and escolhaDoPc == "PEDRA":
        print("Você perdeu.")
    elif opcao == "TESOURA" and escolhaDoPc == "PAPEL":
        print("Você ganhou.")
    if opcao == "TESOURA" and escolhaDoPc == "TESOURA":
        print("Você empatou.")

    
    return


print("Bem vindo ao pedra papel e tesoura!")
escolha = int(input("Insira o número 1 para escolher pedra, número 2 para escolher papel e número 3 para escolher tesoura:"))
jogo(escolha)