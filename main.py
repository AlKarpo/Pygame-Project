import pygame
import random


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
        elif 250 < x < 350 and 430 < y < 470:
            pygame.draw.line(screen, (80, 255, 100), (245, 475), (350, 475), 3)
        elif 250 < x < 350 and 500 < y < 540:
            pygame.draw.line(screen, (80, 255, 100), (245, 545), (350, 545), 3)
        else:
            screen.fill('black')
            meu.display_main_menu(screen)

    def get_coord(self, mouse_pos):
        self.x, self.y = mouse_pos
        return self.x, self.y


class Board:

    def __init__(self):
        self.width = width = 50
        self.height = height = 50
        self.board = [['black'] * width for _ in range(height)]

        self.left = 100
        self.top = 100
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        font = pygame.font.Font(None, 50)
        text = font.render("Coming soon", True, (100, 255, 100))
        text_x = 500 // 2 - text.get_width() // 2
        text_y = 500 // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)


pygame.init()
size = 600, 800
next = False
screen = pygame.display.set_mode(size)
meu = Menu()
screen.fill((0, 0, 0))
meu.display_main_menu(screen)
pygame.display.set_caption('Дедушка сапёра')
running = True
checker = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and checker:
            meu.choosing_punkt(event.pos)
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
pygame.quit()
