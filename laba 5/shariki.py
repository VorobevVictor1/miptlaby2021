from random import randint, choice

import pygame
from pygame.draw import *

FPS = 30
WIDTH = 1000
HEIGHT = 800
Balls_rad_min = 20
Balls_rad_max = 35
COLORS = [(255, 0, 255), (255, 255, 0)]
balls_number = 10
pool = list()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


class Balls:
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
            return 1
        else:
            return 0


pygame.display.update()
clock = pygame.time.Clock()
finished = False

cooldown_pool = [(0, 0), 0]
score = 0
for i in range(balls_number):
    pool.append(Balls())
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            for i, ball in enumerate(pool):
                score += ball.point(click_x, click_y)
                if ball.point(click_x, click_y) == 1:
                    cooldown_pool[0] = event.pos
                    cooldown_pool[1] = 10
                    pool.pop(i)
                    pool.append(Balls())
    if cooldown_pool[1] > 0:
        score_surface = myfont.render('+1', False, (255, 255, 255))
        screen.blit(score_surface, cooldown_pool[0])
        cooldown_pool[1] -= 1
    for ball in pool:
        ball.draw(screen)
        ball.move()
        ball.collision()
    pygame.display.update()
    screen.fill((0, 0, 0))
    score_line = str(score)
    total_score_surface = myfont.render('Score: ' + score_line, False, (255, 255, 255))
    screen.blit(total_score_surface, (0, 0))
print(score)
pygame.quit()
