from turtle import *

ta = Turtle()
ta.speed(20)
bgcolor("gray")

#funcao que recebe x, y (posições no eixo x e y do retangulo a ser formado), e a cor para gerar um retangulo
def retangulo(cor, x, y):
    ta.penup()
    ta.goto(x, y)
    ta.pendown()
    ta.color(cor)
    ta.begin_fill()
    for i in range(2):
        ta.forward(250)
        ta.right(90)
        ta.forward(50)
        ta.right(90)
    ta.end_fill()
    ta.penup()


#bandeira da alemanha
retangulo("yellow", 100, 0)
retangulo("red", 100, 50)
retangulo("black", 100, 100)

#bandeira da hungria
retangulo("green", -300, 0)
retangulo("white", -300, 50)
retangulo("red", -300, 100)

#bandeira da estonia
retangulo("white", -100, 200)
retangulo("black", -100, 250)
retangulo("blue", -100, 300)

done()
