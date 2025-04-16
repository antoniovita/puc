from turtle import *

ta = Turtle()
ta.speed(20)

def planoCartesiano():
    ta.penup() 
    ta.setposition(0, 0)
    ta.pendown()
    ta.left(90)
    ta.forward(300)
    ta.penup()
    ta.goto(0,0)
    ta.left(90) 
    ta.pendown()
    ta.forward(-300)
    ta.penup() 
    ta.setposition(0, 0)
    ta.pendown()
    ta.right(90)
    ta.forward(-300)
    ta.penup()
    ta.goto(0,0)
    ta.left(90)
    ta.pendown()
    ta.forward(300)


def quadrado():
    ta.penup()
    ta.goto(30,30)
    ta.right(90)
    for i in range(4):
        ta.pendown()
        ta.forward(50)
        ta.right(90)

def triangulo():
    ta.penup()
    ta.goto(30,-30)
    ta.right(90)
    for i in range(3):
        ta.pendown()
        ta.forward(50)
        ta.right(120)        


def circulo():
    ta.penup()
    ta.goto(-30,-60)
    ta.left(90)
    ta.pendown()
    ta.circle(30)    


def espiral_octagonal(t, tamanho, angulo, repetições):
    for i in range(repetições):
        ta.forward(tamanho)
        ta.right(angulo)
        tamanho += 0.6




planoCartesiano()
quadrado()
triangulo()
circulo()


ta.penup()
ta.goto(-50, 60)  
ta.pendown()
espiral_octagonal(ta, 1, 45, 40)

ta.penup()
ta.goto(-120,60)
ta.pendown()
espiral_octagonal(ta, 1, 45, 40)


ta.hideturtle()

done()