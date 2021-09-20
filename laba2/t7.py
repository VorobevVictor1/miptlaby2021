import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for i in range(0, 360*5):
    turtle.goto(i/36*np.cos(i/180*np.pi), i/36*np.sin(i/180*np.pi))
    turtle.left(1)

