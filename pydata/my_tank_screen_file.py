import pygame
import sys

from pydata import settings01
from main01 import menu_screen

window_width, window_height = settings01.WIDTH, settings01.HEIGHT
gray = (200, 200, 200)


def my_tank_screen():
    pass


def draw_tabs(screen, current_tab):
    font = pygame.font.SysFont('Comic Sans MS', 30)

    tabs = ["Танк", "Детали", "Оружие"]
    tab_width = window_width // len(tabs) + 1

    # Кнопка "назад"
    back_btn_rect = pygame.Rect(10, 670, 80, 40)
    back_btn = font.render('Back', True, 'black')
    pygame.draw.rect(screen, 'white', back_btn_rect, border_radius=5)
    screen.blit(back_btn, back_btn.get_rect(center=(50, 690)))

    for i, tab in enumerate(tabs):
        tab_rect = pygame.Rect(i * tab_width, 0, tab_width, 50)
        color = gray if i == current_tab else (255, 255, 255)
        pygame.draw.rect(screen, color, tab_rect)

        text = font.render(tab, True, (0, 0, 0))
        text_rect = text.get_rect(center=(i * tab_width + tab_width // 2, 25))
        screen.blit(text, text_rect)


def tank_tab(screen):
    # Логика вкладки "Танк"
    pass


def details_tab(screen):
    # Логика вкладки "Детали"
    pass


def weapon_tab(screen):
    # Логика вкладки "Оружие"
    pass


def main_loop(screen):
    current_tab = 0
    background = pygame.image.load('data/screens/blank_screen_background.png')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y <= 50:
                    current_tab = x // (window_width // 3)
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in pygame.Rect(10, 670, 80, 40):
                    menu_screen()

        # Отображение фона окна
        screen.blit(background, (0, 0))

        # Отображение вкладок и их содержимого
        draw_tabs(screen, current_tab)

        if current_tab == 0:
            tank_tab(screen)
        elif current_tab == 1:
            details_tab(screen)
        elif current_tab == 2:
            weapon_tab(screen)

        pygame.display.flip()
