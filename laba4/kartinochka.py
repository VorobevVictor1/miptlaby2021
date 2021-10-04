import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1032, 768))

"""Во всех фунцкиях х и у --- начальная точка, аналог х0 и у0"""


def dy(y1, y0, scale):
    return int((y1 - y0) * scale)


def dx(x1, x0, ko, scale):
    return int(ko * (x1 - x0) * scale)


def chuvak(x, y, orientacia, scale):
    """чувак
        Туловище,голова, руки, ноги, ступни """
    x0 = 330
    y0 = 215
    if orientacia == 1:
        koef_orientacii = 1
        ko = koef_orientacii
    else:
        koef_orientacii = -1
        ko = koef_orientacii

    ellipse(screen, (167, 147, 172), (x + dx(255, x0, ko, scale), y + dy(230, y0, scale), ko * 150 * scale, 350 * scale))
    circle(screen, (244, 227, 215), (x + dx(330, x0, ko, scale), y + dy(215, y0, scale)), int(50 * scale))
    line(screen, (0, 0, 0), (x + dx(285, x0, ko, scale), y + dy(275, y0, scale)), (x + dx(140, x0, ko, scale),
                                                                                   y + dy(400, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(375, x0, ko, scale), y + dy(275, y0, scale)), (x + dx(500, x0, ko, scale),
                                                                                   y + dy(400, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(290, x0, ko, scale), y + dy(550, y0, scale)), (x + dx(210, x0, ko, scale),
                                                                                   y + dy(700, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(368, x0, ko, scale), y + dy(550, y0, scale)), (x + dx(425, x0, ko, scale),
                                                                                   y + dy(700, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(210, x0, ko, scale), y + dy(700, y0, scale)), (x + dx(130, x0, ko, scale),
                                                                                   y + dy(710, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(425, x0, ko, scale), y + dy(700, y0, scale)), (x + dx(510, x0, ko, scale),
                                                                                   y + dy(710, y0, scale)), 1)


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

    polygon(screen, (255, 204, 0), [(x + dx(155, x0, ko, scale), y + dy(415, y0, scale)), (x + dx(80, x0, ko, scale),
                                                                                           y + dy(380, y0, scale)),
                                    (x + dx(125, x0, ko, scale), y + dy(335, y0, scale))])
    circle(screen, (85, 0, 0), (x + dx(90, x0, ko, scale), y + dy(365, y0, scale)), int(r * scale))
    circle(screen, (255, 0, 0), (x + dx(110, x0, ko, scale), y + dy(345, y0, scale)), int(r * scale))
    circle(screen, (255, 255, 255), (x + dx(85, x0, ko, scale), y + dy(340, y0, scale)), int(r * scale))


def chuviha(x, y, orientacia, scale):
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

    polygon(screen, (255, 85, 221), [(x + dx(700, x0, ko, scale), y + dy(215, y0, scale)),
                                     (x + dx(600, x0, ko, scale), y + dy(580, y0, scale)),
                                     (x + dx(800, x0, ko, scale), y + dy(580, y0, scale))])
    circle(screen, (244, 227, 215), (x + dx(700, x0, ko, scale), y + dy(215, y0, scale)), int(50 * scale))
    line(screen, (0, 0, 0), (x + dx(685, x0, ko, scale), y + dy(275, y0, scale)), (x + dx(500, x0, ko, scale),
                                                                                   y + dy(400, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(715, x0, ko, scale), y + dy(275, y0, scale)),
         (x + dx(800, x0, ko, scale), y + dy(338, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(800, x0, ko, scale), y + dy(338, y0, scale)),
         (x + dx(885, x0, ko, scale), y + dy(270, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(670, x0, ko, scale), y + dy(580, y0, scale)),
         (x + dx(670, x0, ko, scale), y + dy(700, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(730, x0, ko, scale), y + dy(580, y0, scale)),
         (x + dx(730, x0, ko, scale), y + dy(700, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(670, x0, ko, scale), y + dy(700, y0, scale)),
         (x + dx(610, x0, ko, scale), y + dy(700, y0, scale)), 1)
    line(screen, (0, 0, 0), (x + dx(730, x0, ko, scale), y + dy(700, y0, scale)),
         (x + dx(790, x0, ko, scale), y + dy(705, y0, scale)), 1)


def sharik(x, y, orientacia, scale):
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

    line(screen, (0, 0, 0), (x + dx(880, x0, ko, scale), y + dy(300, y0, scale)),
         (x + dx(900, x0, ko, scale), y + dy(150, y0, scale)), 1)
    polygon(screen, (255, 0, 0),
            [(x + dx(900, x0, ko, scale), y + dy(155, y0, scale)), (x + dx(880, x0, ko, scale), y + dy(65, y0, scale)),
             (x + dx(
                 950, x0, ko, scale), y + dy(
                 80, y0, scale))])
    circle(screen, (255, 0, 0), (x + dx(935, x0, ko, scale), y + dy(70, y0, scale)), int(21 * scale))
    circle(screen, (255, 0, 0), (x + dx(899, x0, ko, scale), y + dy(60, y0, scale)), int(21 * scale))


"""Фон
Небо, земля"""
rect(screen, (170, 238, 255), (0, 0, 1032, 384))
rect(screen, (55, 200, 113), (0, 380, 1032, 384))

chuvak(400, 330, 1, 1)
chuvak(1032 - 240, 330, -1, 0.5)
chuviha(425, 330, 1, 0.5)
chuviha(1032 - 425, 330, -1, 0.5)
sharik(150, 430, -1, 1 / 1.5)
morozhka(885, 425, -1, 1 / 1.5)

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
