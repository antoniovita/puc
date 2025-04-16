from turtle import *

t = Turtle()
t.speed(20)
bgcolor("gray")

#criei uma funcao para criar um retangulo que recebe os valores de x, y e cor, sua posicão e cor respectivamente
def rentangulo(x, y, cor):
    t.penup()
    t.goto(x, y)
    t.color(cor)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.forward(200)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

#criei uma funcao para criar um circulo que recebe os valores de x, y, raio e cor, sua posicão, raio e cor respectivamente
def circulo(x, y, raio, cor):
    t.penup()
    t.color(cor)
    t.goto(x, y - raio)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

#criei uma funcao para criar uma estrela que recebe os valores de x, y, tamanho e cor, sua posicão, tamanho e cor respectivamente
def estrela(x, y, tamanho, cor):
    t.penup()
    t.goto(x, y)
    t.color(cor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
        t.forward(tamanho)
        t.right(72)
    t.end_fill()

#criei uma funcao para criar uma estrela de muitas pontas que recebe os parametros x, y (posição), seu tamanho e cor
#ela é uma estrela de 8 pontas, então ela tem um angulo de 135 graus
def estrela2(x, y, tamanho, cor):
    t.penup()
    t.goto(x, y)
    t.color(cor)
    t.setheading(0)
    t.pendown()
    t.fillcolor(cor)
    t.begin_fill()
    for _ in range(8):
        t.forward(tamanho)
        t.left(135)
    t.end_fill()


#aqui estao as funcoes das bandeiras cada uma chamando uma das outras funcoes das formas geometricas
#para fazer a lua eu utilizei dois circulos sobrepostos com cores diferentes

def azerbaijao():
    rentangulo(-100, 0, "green")
    rentangulo(-100, 50, "red")
    rentangulo(-100, 100, "blue")
    circulo(0, 25, 15, "white")
    circulo(7, 28, 12, "red")
    estrela2(18, 25, 12, "white")

def ghana ():
    rentangulo(-100, 0, "green")
    rentangulo(-100, 50, "yellow")
    rentangulo(-100, 100, "red")
    t.penup()
    t.fillcolor("black")
    t.begin_fill()
    estrela(-3, 25, 20, "black")
    t.end_fill()

def turquia ():
    rentangulo(-100, 0, "red")
    rentangulo(-100, 50, "red")
    rentangulo(-100, 100, "red")
    circulo(-3, 25, 24, "white")
    circulo(4, 28, 20, "red")
    estrela(24, 28, 15, "white")

def tunisia ():
    rentangulo(-100, 0, "red")
    rentangulo(-100, 50, "red")
    rentangulo(-100, 100, "red")
    circulo(0, 25, 30, "white")
    circulo(0, 25, 24, "red")
    circulo(7, 28, 16, "white")
    estrela(10, 30, 12, "red")

def niger ():
    rentangulo(-100, 0, "green")
    rentangulo(-100, 50, "white")
    rentangulo(-100, 100, "orange")
    circulo(0, 25, 15, "orange")

def libia ():
    rentangulo(-100, 0, "green")
    rentangulo(-100, 50, "black")
    rentangulo(-100, 100, "red")
    circulo(0, 25, 18, "white")
    circulo(7, 25, 14, "black")
    estrela(20, 25, 10, "white")

def india():
    rentangulo(-100, 0, "green")
    rentangulo(-100, 50, "white")
    rentangulo(-100, 100, "orange")
    circulo(0, 25, 18, "blue")
    circulo(0, 25, 15, "white")
    estrela2(-12, 20, 26, "blue")
    estrela2(-6, 22, 13, "white")

azerbaijao()
ghana()
turquia()
tunisia()
niger()
libia()
india()

t.hideturtle()
done()
