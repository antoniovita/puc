import time

def geraCartelas():

    cartelas = [[] for _ in range(6)]
    
    headers = [1, 2, 4, 8, 16, 32]
    
    for i in range(6):
        cartelas[i].append(headers[i])

    for num in range(1, 64):
        for i, power in enumerate(headers):
            if num & power:
                cartelas[i].append(num)
    
    return cartelas

def exibeCartela(cartela, num_cartela):
    """
    Exibe uma cartela (lista com 32 números) em 4 linhas de 8 números cada.
    """
    print(f"\nCartela {num_cartela}:")
    for i in range(0, len(cartela), 8):
        for n in cartela[i:i+8]:
            print(f"{n:>3}", end=" ")
        print()

def exibeMensagemInicial():
    """
    Exibe a mensagem inicial do jogo.
    """
    print("*************************************************************")
    print("* Jogo da adivinhação                                      *")
    print("* Pense em um inteiro de 1 a 63 e não conte pra ninguém!   *")
    print("* Em seguida, tecle ENTER para continuar... e boa sorte!   *")
    print("*************************************************************")
    input()

def main():
    # Exibe a mensagem inicial e espera pressionar ENTER
    exibeMensagemInicial()
    
    # Gera as 6 cartelas
    cartelas = geraCartelas()
    
    # Variável que irá guardar o palpite final do número escolhido pelo usuário.
    palpite = 0
    headers = [1, 2, 4, 8, 16, 32]
    
    # Para cada cartela, exibe-a e pergunta se o número pensado aparece nela.
    for i, cartela in enumerate(cartelas, start=1):
        exibeCartela(cartela, i)
        resp = input("O seu número está nesta cartela? (S/N): ").strip().upper()
        if resp == "S":
            palpite += headers[i-1]
        print()  # Linha em branco para espaçamento entre as cartelas
        # Opcional: pode-se adicionar um pequeno delay para suspense
        time.sleep(1)
    
    print("Procesando...")
    time.sleep(2)  # suspense
    print(f"\nO número que você escolheu é: {palpite}\n")

if __name__ == '__main__':
    main()