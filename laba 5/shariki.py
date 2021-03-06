from random import randint, choice

import pygame
from pygame.draw import *

FPS = 15
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.font.init()
MYFONT = pygame.font.SysFont('Comic Sans MS', 30)

BALLS_RAD_MIN = 20
BALLS_RAD_MAX = 35
BALLS_V_MIN = 5
BALLS_V_MAX = 7
COLORS_BALLS = [(255, 0, 255), (255, 255, 0)]

SQUARES_SIDE_MIN = 2 * (BALLS_RAD_MIN - 5)
SQUARES_SIDE_MAX = 2 * (BALLS_RAD_MAX - 10)
COLORS_SQUARES = [(123, 176, 50), (8, 190, 205)]

BALLS_NUMBER = 10
SQUARES_NUMBER = BALLS_NUMBER // 2
POOL = list()

LEADERBOARD_FILE = 'leaderboard.txt'


class Balls:
    def __init__(self):
        '''
        Создает мишень-круг: x,y --- координаты центра; v_x, v_y --- скорость по x и y; r --- радиус круга;
        color --- цвет мишени
        '''
        self.x = randint(BALLS_RAD_MAX + 1, WIDTH - BALLS_RAD_MAX - 1)
        self.y = randint(BALLS_RAD_MAX + 1, HEIGHT - BALLS_RAD_MAX - 1)
        self.v_x = randint(BALLS_V_MIN, BALLS_V_MAX) * choice([-1, 1])
        self.v_y = randint(BALLS_V_MIN, BALLS_V_MAX) * choice([-1, 1])
        self.r = randint(BALLS_RAD_MIN, BALLS_RAD_MAX)
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
        self.x = randint(SQUARES_SIDE_MAX + 1, WIDTH - SQUARES_SIDE_MAX - 1)
        self.y = randint(SQUARES_SIDE_MAX + 1, HEIGHT - SQUARES_SIDE_MAX - 1)
        self.s = randint(SQUARES_SIDE_MIN, SQUARES_SIDE_MAX)
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
            self.x = randint(SQUARES_SIDE_MAX + 1, WIDTH - SQUARES_SIDE_MAX - 1)
            self.y = randint(SQUARES_SIDE_MAX + 1, HEIGHT - SQUARES_SIDE_MAX - 1)
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


def screen_wipe(screen=SCREEN):
    '''
    Очищает окно игры.
    :param screen: очищаемая поверхность pygame.surface
    :return: nothing
    '''
    rect(screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT))
    pygame.display.update()


# game screen_functions
def pool_generator(pool=POOL, b_number=BALLS_NUMBER, sq_number=SQUARES_NUMBER):
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


def hit_check(event, cooldown_pool, pool=POOL):
    '''
    Проверяет все мишени из POOL на попадание по ним кликом мышки pygame.event.
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
        score_surface = MYFONT.render('+' + cooldown_pool[2], False, (255, 255, 255))
        SCREEN.blit(score_surface, cooldown_pool[0])
        cooldown_pool[1] -= 1


def gamescreen_update(score, pool=POOL):
    '''
    Обновляет изображение на экране
    :param score: int счет игрока.
    :param pool: list с мишенями
    :return: nothing
    '''
    for target in pool:
        if isinstance(target, Balls):
            target.draw(SCREEN)
            target.move()
            target.collision()
        else:
            target.draw(SCREEN)
            target.move()
    pygame.display.update()
    SCREEN.fill((0, 0, 0))
    total_score_surface = MYFONT.render('Score: ' + str(score), False, (255, 255, 255))
    SCREEN.blit(total_score_surface, (0, 0))


def play(finished, clock, pool, cooldown_pool, score,
         b_number=BALLS_NUMBER, sq_number=SQUARES_NUMBER, FPS=FPS, screen=SCREEN):
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
    :param screen: поверхность pygame.surface, на которой происходит отрисовка игры
    :return: score --- количесвто очков, набранное игроком, finished --- обновленный параметр,
                                                                отвечающий за завершение функции
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
        gamescreen_update(score)
    return score, finished


# name_screen functions
def name_writer(name, event, screen=SCREEN):
    '''
    Записывает имя пользователя.
    :param name: str имя пользователя
    :param event: событие pygame.event
    :param screen: поверхность, где рисуется имя pygame.surface
    :return:str обновленное имя name
    '''
    if pygame.key.name(event.key) == 'backspace':
        name = name[0:len(name) - 1]
        screen_wipe()
    else:
        name += pygame.key.name(event.key)
    return name


def namescreen_update(name):
    '''
    Обновляет экран записи имени игрока
    :param name: str имя игрока
    :return: nothing
    '''
    name_surf = MYFONT.render(name, False, (255, 255, 255))
    SCREEN.blit(name_surf, (0, 150))
    name_insert_surf = MYFONT.render('Enter your name. Use only lowercase.', False, (255, 255, 255))
    SCREEN.blit(name_insert_surf, (0, 0))
    pygame.display.update()


def name_record(finished, clock, name, screen=SCREEN, FPS=FPS):
    '''
    Функция, овтечающая за экран записи имени игрока.
    :param finished: Boolean отвечает за заферщение функции
    :param clock: pygame.clock отвечает за внутриигровое время
    :param name: str имя игрока
    :param screen: поверхность pygame.surface, на которой происходит отрисовка процесса набора имени.
    :param FPS: int количесвто кадров в секунду
    :return: str обновленную строку name с именем игрока, finished --- обновленный параметр,
                                                                отвечающий за завершение функции
    '''
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
                else:
                    name = name_writer(name, event)
        namescreen_update(name)
    return name, finished


# score_screen_functions
def leaderboard_update(score, name, file=LEADERBOARD_FILE):
    '''
    Обновляет таблицу лидеров.
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
            player_score_surface = MYFONT.render(line, False, (255, 255, 255))
            SCREEN.blit(player_score_surface, (0, y))
            y += 80
    pygame.display.update()


def score_show(finished, clock, name, score, file=LEADERBOARD_FILE, screen=SCREEN, FPS=FPS):
    '''
    Отвечает за отрисовку экрана с таблицей лидеров.
    :param finished: Boolean отвечает за заферщение функции
    :param clock: pygame.clock отвечает за внутриигровое время
    :param name: str имя игрока
    :param score: int счет игрока
    :param file: txt файл с таблицей лидеров
    :param screen: поверхность pygame.surface, на которой происходит отрисовка процесса набора имени.
    :param FPS: int количесвто кадров в секунду
    :return: nothing
    '''
    leaderboard_update(score, name)

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                finished = True
                break
        leaderboard_writer()


if __name__ == '__main__':
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    cooldown_pool = [(0, 0), 0, '']
    score = 0

    score, finished = play(finished, clock, POOL, cooldown_pool, score)

    screen_wipe()

    name = ''
    name, finished = name_record(finished, clock, name)

    screen_wipe()

    score_show(finished, clock, name, score)

    pygame.quit()
