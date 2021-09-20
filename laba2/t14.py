import turtle

def star(n):
    if n % 2 == 1:  #для звезд с нечетным количеством вершин
        turtle.right(90 * (1 - 1 / n))
        for i in range(n):
            turtle.forward(150)
            turtle.right(180 * (1 - 1 / n))
    elif n % 4 == 0:   #для звезд с количесвтом вершин, кратным 4
        turtle.right(90 - 180 / n)
        for i in range(n):
            turtle.forward(150)
            turtle.right(180 - 360 / n)
    else:  #для звезд с количеством вершин, не кратным 4
        print('Я такое не умею(((')
    turtle.penup()
    turtle.home()
    turtle.pendown()


turtle.shape('turtle')

star(5)

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

star(11)
