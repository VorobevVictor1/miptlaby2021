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
nums_d = {}
n = 0
with open('co.txt') as file:
    for line in file:
        cifra = list(line.split())
        for k in range(len(cifra)):
            cifra[k] = cifra[k].split(',')
            for m in 0, 1:
                cifra[k][m] = int(cifra[k][m])*r
            cifra[k] = tuple(cifra[k])
        nums_d[str(n)] = cifra
        n += 1
index = input()
for j in index:
    numer(nums_d[j])

