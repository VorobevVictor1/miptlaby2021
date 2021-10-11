import pygame
from pygame.draw import *
from random import randint, choice

FPS = 30
WIDTH = 1000
HEIGHT = 800
Balls_rad_min = 20
Balls_rad_max = 35
COLORS = [(255, 0, 255), (255, 255, 0)]
balls_number = 10
pool = list()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class balls:
    def __init__(self):
        self.x = randint(Balls_rad_max + 1, WIDTH - Balls_rad_max - 1)
        self.y = randint(Balls_rad_max + 1, HEIGHT - Balls_rad_max - 1)
        self.v_x = randint(5, 10) * choice([-1, 1])
        self.v_y = randint(5, 10) * choice([-1, 1])
        self.r = randint(Balls_rad_min, Balls_rad_max)
        self.color = choice(COLORS)

    def draw(self, surface):
        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def collision(self):
        if self.x <= self.r or WIDTH <= self.x + self.r:
            self.v_x *= -1
        if self.y <= self.r or HEIGHT <= self.y + self.r:
            self.v_y *= -1

    def point(self, x, y):
        if abs(self.x - x) <= self.r and abs(self.y - y) <= self.r:
            print('+1')
            return 1
        else:
            return 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            for i in range(balls_number):
                score += pool[i].point(click_x, click_y)

    for i in range(balls_number):
        pool.append(balls())
        pool[i].draw(screen)
        pool[i].move()
        pool[i].collision()
    pygame.display.update()
    screen.fill((0, 0, 0))
print(score)
pygame.quit()
