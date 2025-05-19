def movimentosHanoi(n):
    if n == 1:
        return 1
    return 2 * movimentosHanoi(n - 1) + 1

print(movimentosHanoi(4))
