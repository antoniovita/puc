from turtle import *

ta = Turtle()
ta.speed(0)
ta.hideturtle()
setup(800, 600)
bgcolor("white")

escala_x = 20
escala_y = 20

def plano():
    ta.color("black")
    ta.pensize(2)

    ta.penup()
    ta.goto(-400, 0)
    ta.pendown()
    ta.goto(400, 0)

    ta.penup()
    ta.goto(0, -300)
    ta.pendown()
    ta.goto(0, 300)
    ta.penup()

def funcao1():
    ta.color("green")
    ta.penup()
    primeiro = True
    for i in range(-10, 11):
        x = i
        y = 2**x
        px = x * escala_x
        py = y * escala_y / 5
        if primeiro:
            ta.goto(px, py)
            ta.pendown()
            primeiro = False
        else:
            ta.goto(px, py)
    ta.penup()

def funcao2():
    ta.color("red")
    ta.penup()
    primeiro = True
    for i in range(-20, 21):
        x = i / 2 
        y = 5 - x**2
        px = x * escala_x
        py = y * escala_y
        if primeiro:
            ta.goto(px, py)
            ta.pendown()
            primeiro = False
        else:
            ta.goto(px, py)
    ta.penup()

def funcao3():
    ta.color("blue")
    ta.penup()
    primeiro = True
    for i in range(-20, 21):
        x = i / 2
        y = x**2 - 5*x + 6
        px = x * escala_x
        py = y * escala_y
        if primeiro:
            ta.goto(px, py)
            ta.pendown()
            primeiro = False
        else:
            ta.goto(px, py)
    ta.penup()

def funcao4():
    ta.color("orange")
    ta.penup()
    primeiro = True
    for i in range(-20, 21):
        x = i / 2
        y = x**3 - x**2 - x + 1
        px = x * escala_x
        py = y * escala_y / 2 
        if primeiro:
            ta.goto(px, py)
            ta.pendown()
            primeiro = False
        else:
            ta.goto(px, py)
    ta.penup()

plano()
funcao1()
funcao2()
funcao3()
funcao4()
done()
