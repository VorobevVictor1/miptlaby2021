from random import *
import turtle


turtle.shape('turtle')
turtle.speed(0)
for i in range(100):
    turtle.forward(randint(1, 20))
    turtle.left(randint(-180, 180))


