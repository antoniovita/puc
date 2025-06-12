import random

pontos_total = 10000
dentro_circulo = 0

for _ in range(pontos_total):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        dentro_circulo += 1

pi = 4 * dentro_circulo / pontos_total
print("Estimativa de π:", pi)

def estimar_raiz3(num_pontos: int = 100000) -> float:
    dentro = 0

    for _ in range(num_pontos):
        x = random.uniform(0, 2)
        if x ** 2 <= 3:
            dentro += 1

    estimativa = 2 * (dentro / num_pontos)
    return estimativa

print("Estimativa de √3:", estimar_raiz3())
