import pygame
import random
import os
import sys
import time


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


def events_checker(run):
    running = run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                figures.moving_left()
            if event.key == pygame.K_RIGHT:
                figures.moving_right()
            if event.key == pygame.K_DOWN:
                figures.update()
    return running


class Board:
    def __init__(self):
        self.board = [['0'] * 10 for i in range(20)]
        print(self.board)

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

        self.azure = pygame.sprite.Sprite()
        self.azure.image = load_image('azure.png')
        self.azure.rect = self.azure.image.get_rect()
        all_sprites.add(self.azure)

        self.yellow = pygame.sprite.Sprite()
        self.yellow.image = load_image('yellow.png')
        self.yellow.rect = self.yellow.image.get_rect()
        all_sprites.add(self.yellow)

        self.orange = pygame.sprite.Sprite()
        self.orange.image = load_image('orange.png')
        self.orange.rect = self.orange.image.get_rect()
        all_sprites.add(self.orange)

        self.red = pygame.sprite.Sprite()
        self.red.image = load_image('red.png')
        self.red.rect = self.red.image.get_rect()
        all_sprites.add(self.red)

        self.purple = pygame.sprite.Sprite()
        self.purple.image = load_image('purple.png')
        self.purple.rect = self.purple.image.get_rect()
        all_sprites.add(self.purple)

        self.green = pygame.sprite.Sprite()
        self.green.image = load_image('green.png')
        self.green.rect = self.green.image.get_rect()
        all_sprites.add(self.green)

        self.sprite.rect.x = 180
        self.sprite.rect.y = 52

    def update(self):
        self.sprite.rect = self.sprite.rect.move(0, 32)

    def moving_left(self):
        self.sprite.rect = self.sprite.rect.move(-32, 0)

    def moving_right(self):
        self.sprite.rect = self.sprite.rect.move(32, 0)


all_sprites = pygame.sprite.Group()
pygame.init()
size = 600, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
figures = Figures()
check_time, plus_time, limit_time = 0, 0.02, 0.5
running = True
clock = pygame.time.Clock()
board = Board()
while running:
    events_checker(running)
    pygame.display.flip()
    screen.fill('black')
    all_sprites.draw(screen)
    check_time += plus_time
    if check_time >= limit_time:
        figures.update()
        check_time = 0
    clock.tick(50)
    board.render(screen)

pygame.quit()
