from random import randint
import turtle


number_of_turtles = 20
steps_of_time_number = 50

turtle.hideturtle()
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.pensize(2)
turtle.goto(-100, 100)
turtle.goto(-100, -100)
turtle.goto(100, -100)
turtle.goto(100, 100)


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.turtlesize(0.1, 0.1, 1)
    unit.goto(randint(-100, 100), randint(-100, 100))

V_x = [randint(-3, 3) for i in range(number_of_turtles)]
V_y = [randint(-3, 3) for i in range(number_of_turtles)]

for i in range(steps_of_time_number):
    number = 0
    for unit in pool:
        unit.goto(unit.xcor() + V_x[number], unit.ycor() + V_y[number])
        if unit.xcor() <= -100:
            unit.goto(-unit.xcor() - 200, unit.ycor())
            V_x[number] = -V_x[number]
        if unit.ycor() <= -100:
            unit.goto(unit.xcor(), -unit.ycor() - 200)
            V_y[number] = -V_y[number]
        if unit.xcor() >= 100:
            unit.goto(-unit.xcor() + 200, unit.ycor())
            V_x[number] = -V_x[number]
        if unit.ycor() >= 100:
            unit.goto(unit.xcor(), -unit.ycor() + 200)
            V_y[number] = -V_y[number]
        number += 1
