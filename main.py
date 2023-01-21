from copy import deepcopy
from random import choice

import pygame

W, H = 10, 20
side = 45
GAME_RES = W * side, H * side
size = 750, 940
DICT = {}

vol = 0.1
pygame.init()
screen = pygame.display.set_mode(size)
board_screen = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()
pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.set_volume(vol)
pygame.mixer.music.play(-1)

figures_coords = [[[-1, 0], [-2, 0], [0, 0], [1, 0]],
                  [[0, -1], [-1, -1], [-1, 0], [0, 0]],
                  [[-1, 0], [-1, 1], [0, 0], [0, -1]],
                  [[0, 0], [-1, 0], [0, 1], [-1, -1]],
                  [[0, 0], [0, -1], [0, 1], [-1, -1]],
                  [[0, 0], [0, -1], [0, 1], [1, -1]],
                  [[0, 0], [0, -1], [0, 1], [-1, 0]]]

colors = [(30, 144, 255), (30, 212, 69), (232, 247, 62), (70, 242, 231), (158, 55, 237), (242, 29, 29),
          (237, 162, 12)]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in r] for r in figures_coords]
for num, i in enumerate(figures):
    DICT[colors[num]] = i

check_time, plus_time, time_limit = 0, 0.02, 0.5

main_font = pygame.font.Font(None, 65)
font = pygame.font.Font(None, 45)

total_score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 600, 4: 1000}


class Menu:

    def display_main_menu(self, screen):
        font_title = pygame.font.Font('data\Teletactile-3zavL.ttf', 75)
        self.font_text = pygame.font.Font('data\Teletactile-3zavL.ttf', 32)
        text_title = font_title.render("Tetris", True, (80, 255, 100))
        text_play = self.font_text.render("Start game", True, (80, 255, 100))
        text_music = self.font_text.render("Music off/on", True, (80, 255, 100))
        text_info = self.font_text.render("Info", True, (80, 255, 100))
        text_x = 115
        text_y = 120
        screen.blit(text_title, (180, 120))
        screen.blit(text_play, (235, 300))
        screen.blit(text_music, (210, 370))
        screen.blit(text_info, (310, 440))
        pygame.draw.line(screen, (80, 255, 100), (145, 200), (580, 200), 5)

    def choosing_punkt(self, mouse_pos):
        x, y = mouse_pos
        if 223 < x < 493 and 290 < y < 330:
            pygame.draw.line(screen, (80, 255, 100), (233, 335), (493, 335), 3)
            meu.display_main_menu(screen)
            pygame.display.flip()
        elif 220 < x < 500 and 360 < y < 400:
            pygame.draw.line(screen, (80, 255, 100), (200, 405), (530, 405), 3)
            meu.display_main_menu(screen)
            pygame.display.flip()
        elif 310 < x < 415 and 430 < y < 470:
            pygame.draw.line(screen, (80, 255, 100), (310, 475), (415, 475), 3)
            meu.display_main_menu(screen)
            pygame.display.flip()
        else:
            meu.display_main_menu(screen)
            pygame.display.flip()

    def get_coord(self, mouse_pos):
        self.x, self.y = mouse_pos
        return self.x, self.y


class Board:
    def __init__(self):
        window = []
        with open("data\window.txt") as file:
            for item in file:
                window.append(list(item)[0:-1])
            window = [[int(x) for x in y] for y in window]
            self.field = window

    def render(self, screen):
        for x in range(W):
            for y in range(H):
                pygame.draw.rect(screen, (30, 30, 30), (side * x, side * y, side, side), 1)

    def draw_field(self, field):
        for y, raw in enumerate(field):
            for x, color in enumerate(raw):
                if color:
                    figure.figure_rect.x, figure.figure_rect.y = x * side, y * side
                    pygame.draw.rect(board_screen, color, figure.figure_rect)
        return field


class Figures:
    def __init__(self, new, next_color='0', next_figure='0'):
        if new:
            self.color, self.next_color = choice(colors), choice(colors)
            self.figure, self.next_figure = deepcopy(DICT[self.color]), deepcopy(DICT[self.next_color])
            self.figure_rect = pygame.Rect(0, 0, side - 1, side - 1)
            self.new_figure = False
            self.new = False
        else:
            self.color = deepcopy(next_color)
            self.figure = deepcopy(next_figure)
            self.new_figure = False
            self.next_color = deepcopy(choice(colors))
            self.next_figure = deepcopy(DICT[self.next_color])
            self.figure_rect = pygame.Rect(0, 0, side - 1, side - 1)

    def check_borders(self, figure, i):
        if self.figure[i].x < 0 or self.figure[i].x > W - 1:
            return False
        elif self.figure[i].y > H - 1 or board.field[self.figure[i].y][self.figure[i].x]:
            return False
        return True

    def move_side(self):
        figure_old = deepcopy(self.figure)
        for i in range(4):
            self.figure[i].x += delta
            if not self.check_borders(self.figure, i):
                self.figure = deepcopy(figure_old)
                return self.figure
        return self.figure

    def move_down(self, check_time, time_limit):
        check_time += plus_time
        if check_time > time_limit:
            check_time = 0
            figure_old = deepcopy(self.figure)
            for i in range(4):
                self.figure[i].y += 1
                if not self.check_borders(self.figure, i):
                    for i in range(4):
                        board.field[figure_old[i].y][figure_old[i].x] = self.color
                    self.new_figure = True
                    time_limit = 0.5
                    return check_time, time_limit
        return check_time, time_limit

    def rotation(self):
        ct = self.figure[0]
        figure_old = deepcopy(self.figure)
        if rotate:
            for i in range(4):
                x = self.figure[i].y - ct.y
                y = self.figure[i].x - ct.x
                self.figure[i].x = ct.x - x
                self.figure[i].y = ct.y + y
                if not self.check_borders(figure, i):
                    self.figure = deepcopy(figure_old)
                    return self.figure
        return self.figure

    def clear_line(self):
        self.score = 0
        line, lines = H - 1, 0
        for row in range(H - 1, -1, -1):
            count = 0
            for i in range(W):
                if board.field[row][i]:
                    count += 1
                board.field[line][i] = board.field[row][i]
            if count < W:
                line -= 1
            else:
                lines += 1
        self.score += scores[lines]

    def draw_figures(self, figure):
        for i in range(4):
            self.figure_rect.x = self.figure[i].x * side
            self.figure_rect.y = self.figure[i].y * side
            pygame.draw.rect(board_screen, self.color, self.figure_rect)
        return self.figure

    def draw_next_figures(self, next_figure):
        for i in range(4):
            self.figure_rect.x = self.next_figure[i].x * side + 380
            self.figure_rect.y = self.next_figure[i].y * side + 130
            pygame.draw.rect(screen, next_color, self.figure_rect)


flPause = False
font_text = pygame.font.Font('data\Teletactile-3zavL.ttf', 26)
score = 0
board = Board()
new = True
next_color = 0
next_figure = 0
figure = Figures(new, next_color, next_figure)
new = figure.new
next_color = deepcopy(figure.next_color)
next_figure = deepcopy(figure.next_figure)
meu = Menu()
next = False
checker = True
meu.display_main_menu(screen)
pygame.display.flip()
while True:
    if figure.new_figure:
        figure = Figures(new, next_color, next_figure)
        next_color = figure.next_color
        next_figure = figure.next_figure
    delta, rotate = 0, False
    screen.fill('black')
    screen.blit(board_screen, (20, 20))
    board_screen.fill('black')
    # delay for full lines
    for i in range(lines):
        pygame.time.wait(200)
    # control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and checker:
            meu.choosing_punkt(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = meu.get_coord(event.pos)
            if event.button == 1 and 223 < x < 493 and 290 < y < 330:
                next = True
                checker = False
                screen.fill((0, 0, 0))
            if event.button == 1 and 220 < x < 500 and 360 < y < 400:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.button == 1 and 310 < x < 415 and 430 < y < 470:
                text_in = font_text.render("And there will be no hints", True, (80, 255, 100))
                screen.blit(text_in, (100, 600))
                text_in = font_text.render("everything is serious here", True, (80, 255, 100))
                screen.blit(text_in, (100, 635))
                text_in = font_text.render("He-he-he", True, (80, 255, 100))
                screen.blit(text_in, (290, 690))
                pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta = -1
            elif event.key == pygame.K_RIGHT:
                delta = 1
            elif event.key == pygame.K_DOWN:
                check_time += 0.5
            elif event.key == pygame.K_SPACE:
                time_limit = 0.02
            elif event.key == pygame.K_UP:
                rotate = True
            elif event.key == pygame.K_1:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_2:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
    if next:
        board.render(board_screen)

        figure.move_side()

        check_time, time_limit = figure.move_down(check_time, time_limit)

        figure.rotation()

        figure.clear_line()

        figure.draw_figures(figure)

        board.draw_field(board.field)

        figure.draw_next_figures(next_figure)

        total_score += figure.score
        text_figure = font_text.render("Next figure:", True, (80, 255, 100))
        screen.blit(text_figure, (490, 75))
        text_info = font_text.render("Score:", True, (80, 255, 100))
        screen.blit(text_info, (550, 370))
        if total_score == 0:
            text_info = font_text.render(f"000", True, (80, 255, 100))
        else:
            text_info = font_text.render(f"{total_score}", True, (80, 255, 100))
        screen.blit(text_info, (570, 420))

        # game over
        for i in range(W):
            if board.field[0][i] != 0:
                text_lose = font_text.render("YOU LOSE!", True, (80, 255, 100))
                screen.blit(text_lose, (520, 620))
                pygame.display.flip()
                pygame.time.wait(2000)
                board.field = [[0 for i in range(W)] for i in range(H)]

        pygame.display.flip()
        clock.tick(60)
