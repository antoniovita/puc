def questao1 (num1, num2):
    if num1 < 10 or num2 > 99:
        return 0
    i = num1
    while i < num2:
        if not i % 10 == 0 and not i % int(i / 10) == 0:
            print(i)
        i += 1


def questao2a (n):
    i = 1
    while i < n:
        if n % i == 0:
            print(i)
        i+=1

def questao2b (num1, num2):
    somaDivisores = 0
    i = 1 
    while i < num1:
        if num1 % i == 0:
            somaDivisores +=i
        i+=1
    if somaDivisores == num2:
        return True
    else:
        return False


def questao3(n):
    duzias = n/12
    excedente = n - int(duzias) * 12
    aster = "*" * int(duzias)
    hashtag = "#" * excedente
    print( f"{aster}{hashtag}")