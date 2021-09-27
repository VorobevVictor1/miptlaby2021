import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (191, 199, 193), (0, 0, 400, 400))

circle(screen, (252, 240, 3), (200, 200), 100)
circle(screen, (0, 0, 3), (200, 200), 101, 1)
circle(screen, (0, 0, 0), (150, 175), 10)
circle(screen, (0, 0, 0), (250, 175), 10)
circle(screen, (252, 0, 0), (150, 175), 25, 15)
circle(screen, (252, 0, 0), (250, 175), 20, 10)
circle(screen, (0, 0, 0), (150, 175), 26, 1)
circle(screen, (0, 0, 0), (250, 175), 21, 1)

rect(screen, (0, 0, 0), (150, 250, 100, 20))

line(screen, (0, 0, 0), (90, 100), (185, 160), 15)
line(screen, (0, 0, 0), (220, 159), (300, 120), 15)

pygame.display.flip()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
