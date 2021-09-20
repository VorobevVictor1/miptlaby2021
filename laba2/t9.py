import turtle
import numpy as np


def nnik(n, R):
    turtle.left(90 + 180 / n)
    for i in range(n):
        turtle.forward(2 * R * np.sin(np.pi / n))
        turtle.left(360 / n)
    turtle.right(90 + 180 / n)

turtle.shape('turtle')
R = 15
for j in range(3, 13):
    turtle.penup()
    turtle.goto(R, 0)
    turtle.pendown()
    nnik(j, R)
    R += 10
