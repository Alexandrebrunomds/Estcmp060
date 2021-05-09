import turtle

wn = turtle.Screen() # Modo em Screen para ativar a tela do código

tess = turtle.Turtle() # Criando o objeto a ser introduzido


def triangle(x, y):

    tess.penup() # Colocar a caneta

    tess.goto(x, y) # Usar o cursor do x para y, em sua posição

    tess.pendown() # Ativar a caneta para desenhar os triângulos
    for i in range(3):

        tess.forward(100) # Mover o cursor há 100 unidades para frente

        tess.left(120) # Mover o cursor há 120 unidade a esquerda

        tess.forward(100) # Mover o cursor 100 unidade para frente


turtle.onscreenclick(triangle, 1) # Uma função especial para não haver correntes e loops

turtle.listen()

turtle.done() # Segurar a tela para executar