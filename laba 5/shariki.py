from random import randint, choice

import pygame
from pygame.draw import *

FPS = 15
WIDTH = 1000
HEIGHT = 800
balls_rad_min = 20
balls_rad_max = 35
balls_v_min = 5
balls_v_max = 7
squares_side_min = 2 * (balls_rad_min - 5)
squares_side_max = 2 * (balls_rad_max - 10)
squares_v_min = 8
squares_v_max = 10
COLORS_BALLS = [(255, 0, 255), (255, 255, 0)]
COLORS_SQUARES = [(123, 176, 50), (8, 190, 205)]
balls_number = 10
squares_number = balls_number // 2
pool = list()
LEADERBOARD_FILE = 'leaderboard.txt'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


class Balls:
    def __init__(self):
        self.x = randint(balls_rad_max + 1, WIDTH - balls_rad_max - 1)
        self.y = randint(balls_rad_max + 1, HEIGHT - balls_rad_max - 1)
        self.v_x = randint(balls_v_min, balls_v_max) * choice([-1, 1])
        self.v_y = randint(balls_v_min, balls_v_max) * choice([-1, 1])
        self.r = randint(balls_rad_min, balls_rad_max)
        self.color = choice(COLORS_BALLS)

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

class Squares:
    def __init__(self):
        self.x = randint(squares_side_max + 1, WIDTH - squares_side_max - 1)
        self.y = randint(squares_side_max + 1, HEIGHT - squares_side_max - 1)
        self.v_x = randint(squares_v_min, squares_v_max) * choice([-1, 1])
        self.v_y = randint(squares_v_min, squares_v_max) * choice([-1, 1])
        self.s = randint(squares_side_min, squares_side_max)
        self.color = choice(COLORS_SQUARES)

    def draw(self, surface):
        rect(surface, self.color, (self.x, self.y, self.s, self.s))

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def collision(self):
        if self.x <= self.s or WIDTH <= self.x + self.s:
            self.v_x *= -1
        if self.y <= self.s or HEIGHT <= self.y + self.s:
            self.v_y *= -1

    def point(self, x, y):
        if 0 <= x - self.x <= self.s and 0 <= y - self.y <= self.s:
            return 5
        else:
            return 0

def leaderboard_update(file=LEADERBOARD_FILE):
    with open(file) as f:
        scores = [[score, '', name, '-']]
        for line in f:
            if line == '':
                break
            else:
                player_line = line.split()
                player_line[3] = int(player_line[3])
                player_line.insert(0, player_line[3])
                player_line.pop()
                scores.append(player_line)
    with open(file, 'w') as f:
        while len(scores) >= 11:
            scores.pop(scores.index(min(scores)))
        for i in range(len(scores)):
            f.write(str(i + 1) + '. ' + max(scores)[2] + ' - ' + str(max(scores)[0]) + '\n')
            scores.pop(scores.index(max(scores)))

def screen_wipe(screen=screen):
    rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

cooldown_pool = [(0, 0), 0]
score = 0
for i in range(balls_number+squares_number):
    if i <= balls_number:
        pool.append(Balls())
    else:
        pool.append(Squares())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'return':
                finished = True
                break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            for i, target in enumerate(pool):
                score += target.point(click_x, click_y)
                if target.point(click_x, click_y) > 0:
                    cooldown_pool[0] = event.pos
                    cooldown_pool[1] = 10
                    pool.pop(i)
                    if target.point(click_x, click_y) == 1:
                        pool.append(Balls())
                        flag = 1
                    else:
                        pool.append(Squares())
                        flag = 5
    if cooldown_pool[1] > 0:
        score_surface = myfont.render('+' + str(flag), False, (255, 255, 255))
        screen.blit(score_surface, cooldown_pool[0])
        cooldown_pool[1] -= 1
    for target in pool:
        target.draw(screen)
        target.move()
        target.collision()
    pygame.display.update()
    screen.fill((0, 0, 0))
    score_line = str(score)
    total_score_surface = myfont.render('Score: ' + score_line, False, (255, 255, 255))
    screen.blit(total_score_surface, (0, 0))

screen_wipe()

name = ''
while finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
            break
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'return':
                finished = False
                break
            name += pygame.key.name(event.key)
            name_surf = myfont.render(name, False, (255, 255, 255))
            screen.blit(name_surf, (0, 150))
    name_insert_surf = myfont.render('Enter your name.', False, (255, 255, 255))
    screen.blit(name_insert_surf, (0, 0))
    pygame.display.update()

leaderboard_update()
screen_wipe()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break
        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'return':
                finished = True
                break
    with open('leaderboard.txt') as f:
        y = 0
        for line in f:
            line = line.replace('\n', '')
            player_score_surface = myfont.render(line, False, (255, 255, 255))
            screen.blit(player_score_surface, (0, y))
            y += 80
    pygame.display.update()
pygame.quit()

