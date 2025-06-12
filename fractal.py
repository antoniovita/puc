import turtle

def fractal(t, tamanho, nivel):
    if nivel == 0:
        for _ in range(3):
            t.forward(tamanho)
            t.left(120)
    else:
        fractal(t, tamanho / 2, nivel - 1)
        t.forward(tamanho / 2)
        fractal(t, tamanho / 2, nivel - 1)
        t.backward(tamanho / 2)
        t.left(60)
        t.forward(tamanho / 2)
        t.right(60)
        fractal(t, tamanho / 2, nivel - 1)
        t.left(60)
        t.backward(tamanho / 2)
        t.right(60)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -150)
t.pendown()

fractal(t, 400, 4)

turtle.done()