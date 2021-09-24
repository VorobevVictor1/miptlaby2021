import turtle

turtle.shape('circle')
turtle.speed(3)

V_x = 10
a_y = -9.81
V_y = 25
x = 0
y = 0.00000000000001

"""Сколько времени хотим моделировать систему"""
print("Введите время наблюдения Т.\n")
T = int(input())
#рисуем землю
turtle.hideturtle()
turtle.goto(500, 0)
turtle.goto(0, 0)
turtle.showturtle()

for t in range(int(T / 0.1)):
    if y <= 0:
        V_y = -V_y
    x += V_x * 0.1
    y += V_y * 0.1 + a_y * 0.1**2 / 2
    V_y += a_y * 0.1
    turtle.goto(x, y)
