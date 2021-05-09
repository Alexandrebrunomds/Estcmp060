import turtle    # Modo de importação para usar a biblioteca turtle.
import math   # Importação da Math para fibonacci e usar algumas funções matemáticas.


def fiboPlot(n):   #Função para atribuir os seus valores.
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Configuração da cor que ficará em destaque em azul.
    x.pencolor("blue")

    # Desenvolvimento do primeiro quadrado.
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    # O início da serie em Fibonacci.
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Termino dos quadros da série.
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        # Processo da série em Fibonacci.
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Início do desenho na série em Fibonacci, a caneta desenhando a espiral.
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # A configuração para a caneta na cor vermelho
    x.pencolor("red")

    # A espiral em Fibonacci.
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b


# O fator tem um significado que expande e multiplica a escala, e gráfico no fator em se.
factor = 1

# Informativo do valor atribuido para executar o programa.

n = int(input('Enter the number of iterations (must be > 1): '))

# Dado inserido é executando a espiral em Fibonacci, é mostra a sequência em sua forma numérica.

if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")