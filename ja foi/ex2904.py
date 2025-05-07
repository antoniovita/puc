def checar (x , y): 
    i = x + 1
    while i < y:
        if i >= 10 and y <= 99 and i % 10 != 0 and i % int(i/10) != 0:
            print(i)
        i +=1
checar(10,99)

            