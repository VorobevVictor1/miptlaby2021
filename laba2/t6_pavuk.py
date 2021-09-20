import turtle

turtle.shape('turtle')
n = int(input())
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.goto(0, 0)
    turtle.left(360 / n)
