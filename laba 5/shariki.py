from random import randint, choice

import pygame
from pygame.draw import *

FPS = 15
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

balls_rad_min = 20
balls_rad_max = 35
balls_v_min = 5
balls_v_max = 7
COLORS_BALLS = [(255, 0, 255), (255, 255, 0)]

squares_side_min = 2 * (balls_rad_min - 5)
squares_side_max = 2 * (balls_rad_max - 10)
squares_v_min = 8
squares_v_max = 10
COLORS_SQUARES = [(123, 176, 50), (8, 190, 205)]

balls_number = 10
squares_number = balls_number // 2
pool = list()

LEADERBOARD_FILE = 'leaderboard.txt'


class Balls:
    def __init__(self):
        '''
        Создает мишень-круг: x,y --- координаты центра; v_x, v_y --- скорость по x и y; r --- радиус круга;
        color --- цвет мишени
        '''
        self.x = randint(balls_rad_max + 1, WIDTH - balls_rad_max - 1)
        self.y = randint(balls_rad_max + 1, HEIGHT - balls_rad_max - 1)
        self.v_x = randint(balls_v_min, balls_v_max) * choice([-1, 1])
        self.v_y = randint(balls_v_min, balls_v_max) * choice([-1, 1])
        self.r = randint(balls_rad_min, balls_rad_max)
        self.color = choice(COLORS_BALLS)

    def draw(self, surface):
        '''
        Рисует мишень-круг
        :param surface: поверхность pygame.surface, на которой рисует
        :return: nothing
        '''
        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        '''
        Двигает мишень-круг
        :return: nothing
        '''
        self.x += self.v_x
        self.y += self.v_y

    def collision(self):
        '''
        Обрабатывает столкновения мишени-круга с границами игрового поля. Если столкновение произошло, то меняет
        значение соответсвующей компоненты скорости на противоволожное.
        :return: nothing
        '''
        if self.x <= self.r or WIDTH <= self.x + self.r:
            self.v_x *= -1
        if self.y <= self.r or HEIGHT <= self.y + self.r:
            self.v_y *= -1

    def hit(self, event):
        '''
        проверяет, попал ли игрок мышкой по мишени-кругу.
        :param event: событие pygame.event
        :return: 1 --- количетво очков, которые надо начислисть, если попал. 0 --- если не попал.
        '''
        if abs(self.x - event.pos[0]) <= self.r and abs(self.y - event.pos[1]) <= self.r:
            return 1
        else:
            return 0


class Squares:
    def __init__(self):
        '''
        Создает мишень-квадрат: x,y --- координаты левого верхнего угла квадрата;
        s --- длина стороны квадрата;count --- счетчик времени положения квадрата на одном месте; color --- цвет мишени
        '''
        self.x = randint(squares_side_max + 1, WIDTH - squares_side_max - 1)
        self.y = randint(squares_side_max + 1, HEIGHT - squares_side_max - 1)
        self.s = randint(squares_side_min, squares_side_max)
        self.color = choice(COLORS_SQUARES)
        self.count = int(1.5 * FPS)

    def draw(self, surface):
        '''
        рисует мишень-квадрат
        :return: nothing
        '''
        rect(surface, self.color, (self.x, self.y, self.s, self.s))

    def move(self):
        '''
        Двигает мишень-квадрат
        :return: nothing
        '''
        self.count -= 1
        if self.count == 0:
            self.x = randint(squares_side_max + 1, WIDTH - squares_side_max - 1)
            self.y = randint(squares_side_max + 1, HEIGHT - squares_side_max - 1)
            self.count = int(1.5 * FPS)

    def hit(self, event):
        '''
        проверяет, попал ли игрок мышкой по мишени-квадрату.
        :param event: событие pygame.event
        :return: 5 --- количетво очков, которые надо начислисть, если попал. 0 --- если не попал.
        '''
        if 0 <= event.pos[0] - self.x <= self.s and 0 <= event.pos[1] - self.y <= self.s:
            return 5
        else:
            return 0


def pool_generator(pool=pool, b_number=balls_number, sq_number=squares_number):
    '''
    Генерит пул мишеней.
    :param pool: list, в котором хранятся мишени
    :param b_number: количество мишеней-шаров
    :param sq_number: количесвто мишеней-квадратов
    :return: nothing
    '''
    for i in range(b_number + sq_number):
        if i < b_number:
            pool.append(Balls())
        else:
            pool.append(Squares())


def hit_check(event, cooldown_pool, pool=pool):
    '''
    Проверяет все мишени из pool на попадание по ним кликом мышки pygame.event.
    При попадании увиличивает score на необходимое число очков, обновляет list cooldown_pool.
    :param event: событие pygame.event
    :param cooldown_pool: list список, овтчеающий за отображение добавленных очков
    :param pool: list список мишеней
    :return: int ads_score --- сколько очков надо добавить к score
    '''
    add_score = 0
    for i, target in enumerate(pool):
        add_score += target.hit(event)
        if target.hit(event) > 0:
            cooldown_pool[0] = event.pos
            cooldown_pool[1] = 10
            pool.pop(i)
            if target.hit(event) == 1:
                pool.append(Balls())
                cooldown_pool[2] = '1'
            else:
                pool.append(Squares())
                cooldown_pool[2] = '5'
    return add_score


def hit_score_show(cooldown_pool):
    '''
    Рисует строку с добавленными очками при попадании по мишени.
    :param cooldown_pool: list список, овтчеающий за отображение добавленных очков
    :return: nothing
    '''
    if cooldown_pool[1] > 0:
        score_surface = myfont.render('+' + cooldown_pool[2], False, (255, 255, 255))
        screen.blit(score_surface, cooldown_pool[0])
        cooldown_pool[1] -= 1


def leaderboard_update(score, name, file=LEADERBOARD_FILE):
    '''
    Обновляет табличцу лидеров.
    :param score: int счет игрока
    :param name: str имя игрока
    :param file: txt файл, в котором записана таблица лидеров.
    :return: nothing
    '''
    with open(file) as f:
        if name == '':
            name = 'noname'
        scores = [[score, '', name, '-']]
        for line in f:
            if line == '' or line == '\n':
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


def leaderboard_writer(file=LEADERBOARD_FILE):
    '''
    выводит таблицу лидеров на экран
    :param file: txt файл с таблицей лидеров
    :return: nothing
    '''
    with open(file) as f:
        y = 0
        for line in f:
            line = line.replace('\n', '')
            player_score_surface = myfont.render(line, False, (255, 255, 255))
            screen.blit(player_score_surface, (0, y))
            y += 80
    pygame.display.update()


def screen_wipe(screen=screen):
    '''
    Очищает окно игры.
    :param screen: очищаемая поверхность pygame.surface
    :return: nothing
    '''
    rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
    pygame.display.update()


def screen_update(score, pool=pool):
    '''
    Обновляет изображение на экране
    :param score: int счет игрока.
    :param pool: list с мишенями
    :return: nothing
    '''
    for target in pool:
        if isinstance(target, Balls):
            target.draw(screen)
            target.move()
            target.collision()
        else:
            target.draw(screen)
            target.move()
    pygame.display.update()
    screen.fill((0, 0, 0))
    total_score_surface = myfont.render('Score: ' + str(score), False, (255, 255, 255))
    screen.blit(total_score_surface, (0, 0))


def play(finished, clock, pool, cooldown_pool, score, FPS=FPS, b_number=balls_number, sq_number=squares_number):
    '''
    Функция отвечающая за сам процесс игры.
    :param finished: Boolean отвечает за заферщение функции
    :param clock: pygame.clock отвечает за внутриигровое время
    :param pool: list список мишеней
    :param cooldown_pool: list список, овтчеающий за отображение добавленных очков
    :param score: int счет игрока
    :param FPS: int количесвто кадров в секунду
    :param b_number: int количество мишеней-кругов
    :param sq_number: int количество мишеней-квадратов
    :return: score ---- количесвто очков, набранное игроком
    '''
    pool_generator()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                finished = True
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                score += hit_check(event, cooldown_pool)
        hit_score_show(cooldown_pool)
        screen_update(score)
    return score, finished


pygame.display.update()
clock = pygame.time.Clock()
finished = False

cooldown_pool = [(0, 0), 0, '']
score = 0

score, finished = play(finished, clock, pool, cooldown_pool, score)

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
            if pygame.key.name(event.key) == 'backspace':
                name = name[0:len(name) - 1]
                screen_wipe()
            else:
                name += pygame.key.name(event.key)
    name_surf = myfont.render(name, False, (255, 255, 255))
    screen.blit(name_surf, (0, 150))
    name_insert_surf = myfont.render('Enter your name. Use only lowercase.', False, (255, 255, 255))
    screen.blit(name_insert_surf, (0, 0))
    pygame.display.update()

leaderboard_update(score, name)
screen_wipe()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            finished = True
            break
    leaderboard_writer()

pygame.quit()
