import turtle


def numer(co):
    for i in co:
        turtle.goto(sp[0] + i[0], i[1])
    sp[0] += 1.5 * r
    turtle.penup()
    turtle.goto(sp[0], sp[1])
    turtle.pendown()


turtle.shape('turtle')
turtle.speed(1)
sp = [0, 0]
r = 20
one = [(-r, -r), (0, 0), (0, -2*r)]
two = [(-r, 0), (0, 0), (0, -r), (-r, -2*r), (0, -2*r)]
three = [(-r, 0), (0, 0), (-r, -r), (0, -r), (-r, -2*r)]
four = [(0, -2*r), (0, -r), (-r, -r), (-r, 0)]
five = [(-r, 0), (-r, -r), (0, -r), (0, -2*r), (-r, -2*r)]
six = [(-r, -r), (-r, -2*r), (0, -2*r), (0, -r), (-r, -r)]
seven = [(-r, 0), (0, 0), (-r, -r), (-r, -2*r)]
eight = [(-r, 0), (-r, -2*r), (0, -2*r), (0, -r), (-r, -r), (0, -r), (0, 0)]
nine = [(-r, 0), (-r, -r), (0, -r), (0, 0), (0, -r), (-r, -2*r)]
zero = [(-r, 0), (-r, -2*r), (0, -2*r), (0, 0)]

nums_d = {'1': one,
          '2': two,
          '3': three,
          '4': four,
          '5': five,
          '6': six,
          '7': seven,
          '8': eight,
          '9': nine,
          '0': zero
          }

index = input()
for k in index:
    numer(nums_d[k])
