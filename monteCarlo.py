import random


#estimando pi

pontos_total = 10000
dentro_circulo = 0

for _ in range(pontos_total):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        dentro_circulo += 1

pi = 4 * dentro_circulo / pontos_total
print("Estimativa de π:", pi)

#estimando raíz de 3

def estimar_raiz3(num_pontos: int = 100000) -> float:
    dentro = 0

    for _ in range(num_pontos):
        x = random.uniform(0, 2)
        if x ** 2 <= 3:
            dentro += 1

    estimativa = 2 * (dentro / num_pontos)
    return estimativa

print("Estimativa de √3:", estimar_raiz3())


#estimando o programa das portas

def simular_monty_hall(trocar_escolha=True, simulacoes=100000):
    vitorias = 0

    for _ in range(simulacoes):
        portas = [0, 1, 2]
        premiada = random.choice(portas)
        escolha_inicial = random.choice(portas)

        portas_restantes = [p for p in portas if p != escolha_inicial and p != premiada]
        porta_aberta = random.choice(portas_restantes)

        if trocar_escolha:
            nova_escolha = [p for p in portas if p != escolha_inicial and p != porta_aberta][0]
        else:
            nova_escolha = escolha_inicial

        if nova_escolha == premiada:
            vitorias += 1

    return vitorias / simulacoes

print(f"Probabilidade de vitória trocando: {simular_monty_hall(True):.4f}")
print(f"Probabilidade de vitória mantendo: {simular_monty_hall(False):.4f}")

# estimando a probabilidade de em um conjunto de 23 pessoas haver pelo menos duas que fazem aniversário no mesmo dia.


def aniversario_duplicado(n_pessoas=23):
    aniversarios = [random.randint(1, 365) for _ in range(n_pessoas)]
    return len(set(aniversarios)) < len(aniversarios)

def estimar_probabilidade_aniversario(simulacoes=100000):
    casos_com_coincidencia = 0

    for _ in range(simulacoes):
        if aniversario_duplicado():
            casos_com_coincidencia += 1

    return casos_com_coincidencia / simulacoes

print(f"Probabilidade de ao menos duas pessoas fazerem aniversário no mesmo dia: {estimar_probabilidade_aniversario():.4f}")
