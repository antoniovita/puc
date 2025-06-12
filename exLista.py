def programa ():
    lnomes = list()
    for i in range (6):
        nome = input("Insira seu nome:")
        lnomes.append(nome)
    print(f"Lista criada: {lnomes}")
    novo = input("Insira seu nome: ")
    while novo != "fim":
       for idx, elem in enumerate(lnomes):
            if novo == elem:
               lnomes[idx] = novo.upper()
               print(lnomes)
               novo = input("Insira seu nome: ")
            else:
               lnomes.append(novo)
               novo = input("Insira seu nome: ")

programa()