'''
Desenhar os dois eixos ortogonais - X e Y;
Devem ser plotadas as seguintes funções matemáticas:
y = √x
y = 1/x
Atenção para ajustar os valores para a faixa das coordenadas do plano catesiano.
Dica: Execute a função com valores adequados e depois multiplique o x e o y por valores constantes para que fiquem visíveis na tela.

'''

from turtle import *

ta = Turtle()
ta.speed(20)

def plano ():
    ta.goto(0,0)
    ta.forward(300)
    ta.goto(0,0)
    ta.left(90)
    ta.forward(300)

    ta.goto(0,0)
    ta.right(180)
    ta.forward(300)
    ta.goto(0,0)
    ta.right(90)
    ta.forward(300)
    ta.penup()

def funcao1 ():
    for i in range(300):
        ta.pendown()
        y = (i**0.5)*5
        ta.goto(i, y)

def funcao2 ():
    ta.goto(0,0)
    for i in range(1, 300):
        ta.pendown()
        y = (1/i)*100
        ta.goto(i, y)

plano()
funcao1()
ta.penup()
funcao2()
done()
