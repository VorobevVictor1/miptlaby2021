import turtle
import numpy as np


def circle(r):
    for i in range(0, 360):
        turtle.forward(np.pi * r / 180)
        turtle.left(1)
    for i in range(0, 360):
            turtle.forward(np.pi * r / 180)
            turtle.right(1)
#для начала работы требуется ввести желаемое количество "крыльев" у бабочки

turtle.shape('turtle')
turtle.speed(0)
n = int(input())
turtle.left(90)
for i in range(n):
     circle(40 + 9*i)