import turtle
import numpy as np


def circle(r):
    for i in range(0, 360):
        turtle.forward(np.pi * r / 180)
        turtle.left(1)
    for i in range(0, 360):
            turtle.forward(np.pi * r / 180)
            turtle.right(1)

def flower(r, n):
    for j in range(3):
        circle(r)
        turtle.left(360 / n)
# для начала работы программы требуется ввести желаемое количество листков у цветочка


turtle.shape('turtle')
turtle.speed(0)
n = int(input())
flower(50, n)


