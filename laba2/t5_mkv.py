import turtle

turtle.shape('turtle')
for i in range(10):
    turtle.penup()
    turtle.goto(5*i, -5*i)
    turtle.pendown()
    for j in range(4):
        turtle.left(90)
        turtle.forward(12+2*5*i)