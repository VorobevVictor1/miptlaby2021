import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1032, 768))

"""Во всех фунцкиях х и у --- начальная точка, аналог х0 и у0"""
def chuvak(x, y, orientacia):
    """чувак
        Туловище,голова, руки, ноги, ступни"""
    x0 = 330
    y0 = 215
    if orientacia == 1:
        koef_orientacii = 1
        ko = koef_orientacii
    else:
        koef_orientacii = -1
        ko = koef_orientacii
    def dy(y1):
            return int((y1 - y0) / 2)
    def dx(x1):
        return int(ko * (x1 - x0) / 2)
    ellipse(screen, (167, 147, 172), (x + dx(255), y + dy(230), ko * 150 // 2, 350 // 2))
    circle(screen, (244, 227, 215), (x + dx(330), y + dy(215)), int(50 / 2))
    line(screen, (0, 0, 0), (x + dx(285), y + dy(275)), (x + dx(140), y + dy(400)), 1)
    line(screen, (0, 0, 0), (x + dx(375), y + dy(275)), (x + dx(500), y + dy(400)), 1)
    line(screen, (0, 0, 0), (x + dx(290), y + dy(550)), (x + dx(210), y + dy(700)), 1)
    line(screen, (0, 0, 0), (x + dx(368), y + dy(550)), (x + dx(425), y + dy(700)), 1)
    line(screen, (0, 0, 0), (x + dx(210), y + dy(700)), (x + dx(130), y + dy(710)), 1)
    line(screen, (0, 0, 0), (x + dx(425), y + dy(700)), (x + dx(510), y + dy(710)), 1)

def morozhka(x, y, orientacia, scale):
    """морожка чувака
        Рожок, левый шарик, правый шарик, вехний шарик"""
    x0 = 155
    y0 = 415
    r = 16
    if orientacia == 1:
        koef_orientacii = 1
        ko = koef_orientacii
    else:
        koef_orientacii = -1
        ko = koef_orientacii
    def dy(y1):
            return int((y1 - y0) * scale)
    def dx(x1):
        return int(ko * (x1 - x0) * scale)
    polygon(screen, (255, 204, 0), [(x + dx(155), y + dy(415)), (x + dx(80), y + dy(380)), (x + dx(125), y + dy(335))])
    circle(screen, (85, 0, 0), (x + dx(90), y + dy(365)), int(r * scale))
    circle(screen, (255, 0, 0), (x + dx(110), y + dy(345)), int(r * scale))
    circle(screen, (255, 255, 255), (x +dx(85), y + dy(340)), int(r * scale))

def chuviha(x, y, orientacia):
    """Чувиха
    Туловище, голова, руки, ноги"""
    x0 = 700
    y0 = 215
    if orientacia == 1:
        koef_orientacii = 1
        ko = koef_orientacii
    else:
        koef_orientacii = -1
        ko = koef_orientacii
    def dy(y1):
        return int((y1 - y0) / 2)
    def dx(x1):
        return int(ko * (x1 - x0) / 2)
    polygon(screen, (255, 85, 221), [(x + dx(700), y + dy(215)),
                                     (x + dx(600), y + dy(580)), (x + dx(800), y + dy(580))])
    circle(screen, (244, 227, 215), (x + dx(700), y + dy(215)), int(50 / 2))
    line(screen, (0, 0, 0), (x + dx(685), y + dy(275)), (x + dx(500), y + dy(400)), 1)
    line(screen, (0, 0, 0), (x + dx(715), y + dy(275)), (x + dx(800), y + dy(338)), 1)
    line(screen, (0, 0, 0), (x + dx(800), y + dy(338)), (x + dx(885), y + dy(270)), 1)
    line(screen, (0, 0, 0), (x + dx(670), y + dy(580)), (x + dx(670), y + dy(700)), 1)
    line(screen, (0, 0, 0), (x + dx(730), y + dy(580)), (x + dx(730), y + dy(700)), 1)
    line(screen, (0, 0, 0), (x + dx(670), y + dy(700)), (x + dx(610), y + dy(700)), 1)
    line(screen, (0, 0, 0), (x + dx(730), y + dy(700)), (x + dx(790), y + dy(705)), 1)

def sharik(x, y, orientacia):
    """Шарик чувихи
    Палка, треугольник, два круга"""
    x0 = 880
    y0 = 300
    if orientacia == 1:
        koef_orientacii = 1
        ko = koef_orientacii
    else:
        koef_orientacii = -1
        ko = koef_orientacii
    def dy(y1):
        return int((y1 - y0) / 1.5)
    def dx(x1):
        return int(ko * (x1 - x0) / 1.5)
    line(screen, (0, 0, 0), (x + dx(880), y + dy(300)), (x + dx(900), y + dy(150)), 1)
    polygon(screen, (255, 0, 0), [(x + dx(900), y + dy(155)), (x + dx(880), y + dy(65)), (x + dx(950), y + dy(80))])
    circle(screen, (255, 0, 0), (x + dx(935), y + dy(70)), int(21 / 1.5))
    circle(screen, (255, 0, 0), (x + dx(899), y + dy(60)), int(21 / 1.5))

"""Фон
Небо, земля"""
rect(screen, (170, 238, 255), (0, 0, 1032, 384))
rect(screen, (55, 200, 113), (0, 380, 1032, 384))

chuvak(240, 330, 1)
chuvak(1032 - 240, 330, -1)
chuviha(425, 330, 1)
chuviha(1032 - 425, 330, -1)
sharik(150, 430, -1)
morozhka(885, 425, -1, 1/1.5)

line(screen, (0, 0, 0), (507, 380), (560, 230), 1)
morozhka(560, 230, 1, 1.5)

pygame.display.flip()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
