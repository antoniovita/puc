from turtle import *

ta = Turtle()
ta.speed(20)

bgcolor('black')

def retangulo(largura, altura, cor):
    color(cor)
    begin_fill()
    for i in range(2):
        forward(largura)
        right(90)
        forward(altura)
        right(90)
    end_fill()

def estrela(largura, altura, cor):
    color(cor)
    begin_fill()
    for _ in range(5):
        forward(largura)
        right(144)
        forward(largura)
        left(72)
    end_fill()


#facil - 2-3 formas
def italia():
    penup()
    goto(-150, 100)
    pendown()
    
    retangulo(100, 200, "green")
    
    penup()
    forward(100)
    pendown()
    retangulo(100, 200, "white")
    
    penup()
    forward(100)
    pendown()
    retangulo(100, 200, "red")

italia()

#media 3-4 formas
def camaroes():

    penup()
    goto(-150, 100)
    pendown()
    
    retangulo(100, 200, "green")
    
    penup()
    forward(100)
    pendown()
    retangulo(100, 200, "red")
    
    penup()
    forward(100)
    pendown()
    retangulo(100, 200, "yellow")

    penup()

    goto(0,10)
    pendown()
    estrela(20,20,"yellow")

camaroes()

#dificil - +4 formas
def coreiaDoNorte():
    penup()
    goto(-200, 100) 
    pendown()
    retangulo(400, 200, "red")

    penup()
    goto(-200, 100) 
    pendown()
    retangulo(400, 40, "blue")

    penup()
    goto(-200, 70) 
    pendown()
    retangulo(400, 10, "white")

    penup()
    goto(-200, -60) 
    pendown()
    retangulo(400, 40, "blue")

    penup()
    goto(-200, -60) 
    pendown()
    retangulo(400, 10, "white")
    
    penup()
    goto(-110, -50)
    pendown()
    color("white")
    begin_fill()
    circle(50)
    end_fill()
    
    penup()
    goto(-100, 10)
    pendown()
    estrela(30, 30, 'red')

coreiaDoNorte()

hideturtle()
done()