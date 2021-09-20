import turtle
import numpy as np


def duga(r):
    for i in range(0, 180):
        turtle.forward(np.pi * r / 180)
        turtle.right(1)
#для начала работы требуется ввести желаеоме количество витков пружины

turtle.shape('turtle')
turtle.speed(0)
n = int(input())
turtle.left(90)
duga(35)
for i in range(n-1):
    duga(5)
    duga(35)