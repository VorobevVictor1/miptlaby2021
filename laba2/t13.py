import turtle


turtle.shape('turtle')
#голова
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
#два глаза
turtle.penup()
turtle.goto(-40, 40)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(40, 40)
turtle.pendown()

turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
#нос
turtle.penup()
turtle.goto(0, 15)
turtle.pendown()

turtle.width(10)
turtle.right(90)
turtle.forward(30)
#рот
turtle.penup()
turtle.goto(40, -25)
turtle.pendown()

turtle.width(15)
turtle.pencolor('red')
turtle.left(180)
turtle.circle(40, -180)








