from turtle import *

speed("fastest")

rt(-90) # Ao configurar isso colocar a tartaruga para cima

angle = 30 # Mudança do ângulo de base para o ramo Y

def y(sz, level):  #funcionar na função Y
    if level > 0:
        colormode(255)

        # Fica dividido os intervalos em RGB, para ficar de acordo com cada nivél do módulo atual
        pencolor(0, 255 // level, 0)

        fd(sz) # Configuração da base

        rt(angle)

        y(0.8 * sz, level - 1) # Recursivo para submeter a base a direita
        pencolor(0,255 // level, 0)
        lt(2 * angle)

        y(0.8 * sz, level -1) # Recursivo para submeter a base a esquerda
        pencolor(0, 255 // level, 0)

        rt(angle)
        fd(-sz)

y(80, 7)
