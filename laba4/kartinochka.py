import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1030, 760))

rect(screen, (170, 238, 255), (0, 0, 1030, 380))
rect(screen, (55, 200, 113), (0, 380, 1030, 380))

"""чувак"""
ellipse(screen, (167, 147, 172), (255, 230, 150, 350))
circle(screen, (244, 227, 215), (330, 215), 50)
line(screen, (0, 0, 0), (285, 275), (140, 400), 2)
line(screen, (0, 0, 0), (375, 275), (500, 400), 2)
line(screen, (0, 0, 0), (290, 550), (210, 700), 2)
line(screen, (0, 0, 0), (368, 550), (425, 700), 2)
line(screen, (0, 0, 0), (210, 700), (130, 710), 2)
line(screen, (0, 0, 0), (425, 700), (510, 710), 2)

"""морожка чувака"""
polygon(screen, (255, 204, 0), [(155, 415), (80, 380), (125, 335)])

pygame.display.flip()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()