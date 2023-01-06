import pygame
import random
import os
import sys

SPEED = 32
FPS = 1
WINDOW = []



class Menu:
    def __init__(self):
        self.width = 500
        self.height = 500

    def display_main_menu(self, screen):
        font_title = pygame.font.Font('data\Teletactile-3zavL.ttf', 75)
        font_text = pygame.font.Font('data\Teletactile-3zavL.ttf', 32)
        text_title = font_title.render("Tetris", True, (80, 255, 100))
        text_play = font_text.render("Start game", True, (80, 255, 100))
        text_settings = font_text.render("Settings", True, (80, 255, 100))
        text_info = font_text.render("Info", True, (80, 255, 100))
        text_exit = font_text.render("Exit", True, (80, 255, 100))
        text_x = 115
        text_y = 120
        screen.blit(text_title, (115, 120))
        screen.blit(text_play, (170, 300))
        screen.blit(text_settings, (200, 370))
        screen.blit(text_info, (245, 440))
        screen.blit(text_exit, (245, 510))
        pygame.draw.line(screen, (80, 255, 100), (80, 200), (515, 200), 5)

    def choosing_punkt(self, mouse_pos):
        x, y = mouse_pos
        if 170 < x < 430 and 290 < y < 330:
            pygame.draw.line(screen, (80, 255, 100), (170, 335), (430, 335), 3)
        elif 195 < x < 410 and 360 < y < 400:
            pygame.draw.line(screen, (80, 255, 100), (195, 405), (410, 405), 3)
        elif 250 < x < 350 and 430 <  y < 470:
            pygame.draw.line(screen, (80, 255, 100), (245, 475), (350, 475), 3)
        elif 250 < x < 350 and 500 < y < 540:
            pygame.draw.line(screen, (80, 255, 100), (245, 545), (350, 545), 3)
        else:
            screen.fill('black')
            meu.display_main_menu(screen)

    def get_coord(self, mouse_pos):
        self.x, self.y = mouse_pos
        return self.x, self.y



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


# def events_checker(run, check):
#    checker = check
#    running = run
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                figures.moving_left()
#            if event.key == pygame.K_RIGHT:
#                figures.moving_right()
#            if event.key == pygame.K_DOWN:
#                figures.update()
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            x, y = meu.get_coord(event.pos)
#            if event.button == 1 and 170 < x < 430 and 290 < y < 330:
#                board = Board()
#                next = True
#                checker = False
#                screen.fill((0, 0, 0))
#        if event.type == pygame.MOUSEMOTION and checker:
#            meu.choosing_punkt(event.pos)
#    return running, checker


class Board:
    def __init__(self):
        with open("data\window.txt") as file:
            for item in file:
                WINDOW.append(list(item)[0:-1])
        print(WINDOW)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (50, 50, 324, 644), 2)


class Figures(pygame.sprite.Sprite):
    image = load_image('blue.png')

    def __init__(self):
        super().__init__()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image('blue.png')
        self.sprite.rect = self.sprite.image.get_rect()
        all_sprites.add(self.sprite)

        #self.azure = pygame.sprite.Sprite()
        #self.azure.image = load_image('azure.png')
        #self.azure.rect = self.azure.image.get_rect()
        #all_sprites.add(self.azure)
#
        #self.yellow = pygame.sprite.Sprite()
        #self.yellow.image = load_image('yellow.png')
        #self.yellow.rect = self.yellow.image.get_rect()
        #all_sprites.add(self.yellow)
#
        #self.orange = pygame.sprite.Sprite()
        #self.orange.image = load_image('orange.png')
        #self.orange.rect = self.orange.image.get_rect()
        #all_sprites.add(self.orange)
#
        #self.red = pygame.sprite.Sprite()
        #self.red.image = load_image('red.png')
        #self.red.rect = self.red.image.get_rect()
        #all_sprites.add(self.red)
#
        #self.purple = pygame.sprite.Sprite()
        #self.purple.image = load_image('purple.png')
        #self.purple.rect = self.purple.image.get_rect()
        #all_sprites.add(self.purple)
#
        #self.green = pygame.sprite.Sprite()
        #self.green.image = load_image('green.png')
        #self.green.rect = self.green.image.get_rect()
        #all_sprites.add(self.green)

        self.sprite.rect.x = 180
        self.sprite.rect.y = 52

    def update(self):
        self.sprite.rect = self.sprite.rect.move(0, 32)

    def moving_left(self):
        self.sprite.rect = self.sprite.rect.move(-32, 0)

    def moving_right(self):
        self.sprite.rect = self.sprite.rect.move(32, 0)


class Board:
    def __init__(self):
        self.board = [['0'] * 10 for i in range(20)]
        print(self.board)

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (50, 50, 324, 644), 3)


all_sprites = pygame.sprite.Group()
pygame.init()
size = 600, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
meu = Menu()
next = False
meu.display_main_menu(screen)
figures = Figures()
check_time, plus_time, limit_time = 0, 0.02, 0.5
running = True
checker = True
clock = pygame.time.Clock()
board = Board()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and checker:
            meu.choosing_punkt(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                figures.moving_left()
            if event.key == pygame.K_RIGHT:
                figures.moving_right()
            if event.key == pygame.K_DOWN:
                figures.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = meu.get_coord(event.pos)
            if event.button == 1 and 170 < x < 430 and 290 < y < 330:
                board = Board()
                next = True
                checker = False
                screen.fill((0, 0, 0))
    if next:
        board.render(screen)
        pygame.display.flip()
        screen.fill('black')
        all_sprites.draw(screen)
        check_time += plus_time
        if check_time >= limit_time:
            figures.update()
            check_time = 0
        clock.tick(50)
        board.render(screen)
    pygame.display.flip()

pygame.quit()
