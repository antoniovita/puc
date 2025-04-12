from turtle import *
import random

ta = Turtle()
ta.speed(20)

def planoCartesiano():
    ta.penup()
    ta.goto(0, 0)
    ta.pendown()
    ta.setheading(90)
    ta.forward(300)
    ta.penup()
    ta.goto(0, 0)
    ta.setheading(270)
    ta.pendown()
    ta.forward(300)
    ta.penup()
    ta.goto(0, 0)
    ta.setheading(0)
    ta.pendown()
    ta.forward(300)
    ta.penup()
    ta.goto(0, 0)
    ta.setheading(180)
    ta.pendown()
    ta.forward(300)
def posicao_aleatoria(quadrante):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    if quadrante == 1:
        return x, y
    elif quadrante == 2:
        return -x, y
    elif quadrante == 3:
        return -x, -y
    elif quadrante == 4:
        return x, -y

def desenha_quadrado(x, y, tamanho, cor):
    ta.penup()
    ta.goto(x, y)
    ta.color(cor)
    ta.pendown()
    for _ in range(4):
        ta.forward(tamanho)
        ta.right(90)

def desenha_triangulo(x, y, tamanho, cor):
    ta.penup()
    ta.goto(x, y)
    ta.color(cor)
    ta.setheading(0)
    ta.pendown()
    for _ in range(3):
        ta.forward(tamanho)
        ta.right(120)

def desenha_circulo(x, y, raio, cor):
    ta.penup()
    ta.goto(x, y - raio)
    ta.setheading(0)
    ta.color(cor)
    ta.pendown()
    ta.circle(raio)

def desenha_espiral(x, y, abertura, cor):
    ta.penup()
    ta.goto(x, y)
    ta.setheading(0)
    ta.color(cor)
    ta.pendown()
    tamanho = 1
    for _ in range(40):
        ta.forward(tamanho)
        ta.right(abertura)
        tamanho += 0.6

cor_quadrado = textinput("Cor", "Digite a cor do quadrado:")
cor_triangulo = textinput("Cor", "Digite a cor do triângulo:")
cor_circulo = textinput("Cor", "Digite a cor do círculo:")
cor_espiral = textinput("Cor", "Digite a cor da espiral:")

planoCartesiano()

x1, y1 = posicao_aleatoria(1)
desenha_quadrado(x1, y1, 50, cor_quadrado)

x2, y2 = posicao_aleatoria(2)
desenha_triangulo(x2, y2, 50, cor_triangulo)

x3, y3 = posicao_aleatoria(3)
desenha_circulo(x3, y3, 30, cor_circulo)

x4, y4 = posicao_aleatoria(4)
desenha_espiral(x4, y4, 50, cor_espiral)

ta.hideturtle()
done()
