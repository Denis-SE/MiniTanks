import numpy as np
import random

import pygame.display
# import sqlite3

from pydata.tanks01 import Tank
from pydata import my_tank01
from pydata.my_tank_screen_file import *
from pydata import settings01

# Инициализация Pygame
pygame.init()

# Размеры окна
window_width, window_height = settings01.WIDTH, settings01.HEIGHT

# Создание окна
screen = pygame.display.set_mode((window_width, window_height))
screen.fill((0, 0, 0))
pygame.display.set_caption("MiniTanks")

# Выбор иконки
game_icon = pygame.image.load('data/screens/game_icon.png')
pygame.display.set_icon(game_icon)

# Создание поверхности
surface = pygame.Surface((screen.get_width(), screen.get_height()))

sky_r = random.randint(0, 255)
sky_g = random.randint(0, 255)
sky_b = random.randint(0, 255)

ground_r = random.randint(0, 255)
ground_g = random.randint(0, 255)
ground_b = random.randint(0, 255)

# surface.fill((sky_r, sky_g, sky_b))
surface.fill(settings01.sky)

# Создание массива для хранения высот поверхности
surface_heights = np.zeros((window_width,))

# Заполнение массива синусоидными значениями
amplitude = settings01.AMPLITUDE  # Амплитуда синусоиды
frequency = settings01.FREQUENCY  # Частота синусоиды

for i in range(window_width):
    surface_heights[i] = amplitude * np.sin(frequency * i) + amplitude + 50

# Создание танка
# tank1 = None
# tank2 = None
# tank3 = None
# tank4 = None
# tank5 = None
# tank6 = None
# tank7 = None
# tank8 = None
# tank9 = None
# tank10 = None
# tanks_play = [['t1', tank1], ['t2', tank2], ['t3', tank3], ['t4', tank4], ['t5', tank5],
#               ['t6', tank6], ['t7', tank7], ['t8', tank8], ['t9', tank9], ['t10', tank10]]
# tanks_in_game = []

tank_count = 2
tank_check = 1

tank1_x = random.randint(10, window_width // 2 - 50)
tank1_hp = 100
all_sprites = pygame.sprite.Group()

tank2_x = random.randint(window_width // 2 + 10, window_width - 50)
tank2_hp = 100

step_hp = 10
step_hp_rect = 300 // 100
# Количество игроков
players_count = 2

# Скорость движения танка
clock = pygame.time.Clock()
tank_speed = my_tank01.speed

# Частота кадров
FPS = settings01.FPS

# Подключение базы данных
# con = sqlite3.connect('mini_tanks_base')
# cur = con.cursor()


# Функция стартового окна
def start_screen():
    start_screen_fon = pygame.transform.scale(pygame.image.load('data/screens/start_screen_background.png'),
                                              (window_width, window_height))
    screen.blit(start_screen_fon, (0, 0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # обработка нажатия на крестик (выход)
                exit()
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                menu_screen()


# Функция основного меню игры
def menu_screen():
    font = pygame.font.SysFont('Comic Sans MS', 30)
    menu_screen_background = pygame.transform.scale(pygame.image.load('data/screens/menu_screen_background.png'),
                                                    (window_width, window_height))
    screen.blit(menu_screen_background, (0, 0))
    start_game_btn_rect = pygame.Rect(470, 220, 380, 50)
    start_game_btn = font.render('Play', True, 'black')
    pygame.draw.rect(screen, 'white', start_game_btn_rect, border_radius=20)
    screen.blit(start_game_btn, start_game_btn.get_rect(center=(660, 245)))

    menu_btn_rect = pygame.Rect(470, 320, 380, 50)
    menu_btn = font.render('Menu', True, 'black')
    pygame.draw.rect(screen, 'white', menu_btn_rect, border_radius=20)
    screen.blit(menu_btn, menu_btn.get_rect(center=(660, 345)))

    settings_btn_rect = pygame.Rect(470, 420, 380, 50)
    settings_btn = font.render('Settings', True, 'black')
    pygame.draw.rect(screen, 'white', settings_btn_rect, border_radius=20)
    screen.blit(settings_btn, settings_btn.get_rect(center=(660, 445)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # обработка нажатия на крестик (выход)
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in start_game_btn_rect:
                    pregame_screen()
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in menu_btn_rect:
                    main_loop(screen)
        pygame.display.flip()
        clock.tick(30)


# def my_tank_screen():
#     pass


# Функция окна перед боем
def pregame_screen():
    # global tanks_in_game
    global players_count
    # global con
    # global cur
    global tank_count

    font = pygame.font.SysFont('Comic Sans MS', 30)
    pregame_screen_background = pygame.transform.scale(pygame.image.load('data/screens/blank_screen_background.png'),
                                                       (window_width, window_height))
    screen.blit(pregame_screen_background, (0, 0))

    left_darkened_screen_rect = pygame.Rect(0, 0, window_width // 2, window_height)
    left_dark_rect = pygame.Surface(pygame.Rect(left_darkened_screen_rect).size, pygame.SRCALPHA)
    pygame.draw.rect(left_dark_rect, (0, 0, 0, 125), left_dark_rect.get_rect())
    screen.blit(left_dark_rect, left_darkened_screen_rect)

    right_darkened_screen_rect = pygame.Rect(window_width // 2, 0, window_width // 2, window_height)
    right_dark_rect = pygame.Surface(pygame.Rect(right_darkened_screen_rect).size, pygame.SRCALPHA)
    pygame.draw.rect(right_dark_rect, (0, 0, 0, 175), right_dark_rect.get_rect())
    screen.blit(right_dark_rect, right_darkened_screen_rect)

    settings_label_rect = pygame.Rect(window_width // 2 + 25, 25, 160, 50)
    settings_label_text = font.render('Settings:', True, 'black')
    pygame.draw.rect(screen, 'white', settings_label_rect, border_radius=20)
    screen.blit(settings_label_text, settings_label_text.get_rect(center=(740, 47)))

    players_label_rect = pygame.Rect(25, 25, 160, 50)
    players_label_text = font.render('Players:', True, 'black')
    pygame.draw.rect(screen, 'white', players_label_rect, border_radius=20)
    screen.blit(players_label_text, players_label_text.get_rect(center=(95, 47)))

    start_game_btn_rect = pygame.Rect(1090, window_height - 90, 150, 50)
    start_game_btn = font.render('Battle!', True, 'black')
    pygame.draw.rect(screen, 'white', start_game_btn_rect, border_radius=20)
    screen.blit(start_game_btn, start_game_btn.get_rect(center=(1165, window_height - 65)))

    up_players_btn_rect = pygame.Rect(1185, 520, 50, 50)
    up_players_btn = font.render('>', True, 'black')
    pygame.draw.rect(screen, 'white', up_players_btn_rect, border_radius=5)
    screen.blit(up_players_btn, up_players_btn.get_rect(center=(1210, 542)))

    down_players_btn_rect = pygame.Rect(1090, 520, 50, 50)
    down_players_btn = font.render('<', True, 'black')
    pygame.draw.rect(screen, 'white', down_players_btn_rect, border_radius=5)
    screen.blit(down_players_btn, down_players_btn.get_rect(center=(1115, 542)))

    count_players_btn_rect = pygame.Rect(1120, 520, 70, 50)
    count_players_btn = font.render(str(players_count), True, 'black')
    pygame.draw.rect(screen, 'white', count_players_btn_rect)
    screen.blit(count_players_btn, count_players_btn.get_rect(center=(1155, 542)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # обработка нажатия на крестик (выход)
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in start_game_btn_rect:
                    # tanks_in_game = tanks_play[:players_count]
                    # for t in tanks_in_game:
                    #     print(tanks_in_game)
                    #     x = random.randint(10, window_width - 50)
                    #     cur.execute(f'insert into base_in_game(tank, x_coord, y_coord, hp)
                    #       values({str(t[0])}, x, 0, 100)')
                    #     con.commit()
                    # tank_count = players_count
                    game()
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in up_players_btn_rect:
                    if players_count < 10:
                        players_count += 1
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in down_players_btn_rect:
                    if players_count > 2:
                        players_count -= 1
        count_players_btn_rect = pygame.Rect(1120, 520, 70, 50)
        count_players_btn = font.render(str(players_count), True, 'black')
        pygame.draw.rect(screen, 'white', count_players_btn_rect)
        screen.blit(count_players_btn, count_players_btn.get_rect(center=(1155, 542)))
        pygame.display.flip()
        clock.tick(30)


# Функция окна с результатами
def final_screen(text):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    pregame_screen_background = pygame.transform.scale(pygame.image.load('data/screens/blank_screen_background.png'),
                                                       (window_width, window_height))
    screen.blit(pregame_screen_background, (0, 0))

    result_rect = pygame.Rect(470, 120, 380, 50)
    result = font.render(text, True, 'black')
    pygame.draw.rect(screen, 'white', result_rect, border_radius=20)
    screen.blit(result, result.get_rect(center=(660, 145)))

    continue_rect = pygame.Rect(470, 220, 380, 50)
    continue_button = font.render('Continue', True, 'black')
    pygame.draw.rect(screen, 'white', continue_rect, border_radius=20)
    screen.blit(continue_button, continue_button.get_rect(center=(660, 245)))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # обработка нажатия на крестик (выход)
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect(event.pos[0], event.pos[1], 1, 1) in continue_rect:
                    pregame_screen()


# Функция выстрела
def shot(tank, mouse_x, mouse_y):
    global tank1_x
    global tank1_hp
    global tank2_x
    global tank2_hp

    bullet_x, bullet_y = tank.tanks_bullet()
    # print(bullet_x, bullet_y)
    bullet_surf = pygame.image.load("data/bullets_sprite/bullet_blue.png")
    bullet_circle = bullet_surf.get_rect(center=(bullet_x, bullet_y))
    screen.blit(bullet_surf, bullet_circle)
    pygame.display.update()
    clock.tick(FPS)
    diff_x = mouse_x - bullet_x
    step_x = 0
    if diff_x > 0:
        step_x = 1
    elif diff_x < 0:
        step_x = -1
        diff_x *= -1
    else:
        step_x = 0
    diff_y = mouse_y - bullet_y
    if step_x != 0:
        step_y = diff_y / diff_x
    else:
        step_y = 1
    new_x = bullet_x
    # new_y = bullet_y
    # Полёт снаряда пока он не коснётся поверхности земли или не вылетит за пределы окна
    while (bullet_y < window_height - surface_heights[bullet_x] - settings01.up_ground) and (new_x < window_width):
        # print(mouse_y, bullet_y)
        # print(new_y, settings.HEIGHT - surface_heights[new_x])
        last_y = bullet_y
        bullet_x += step_x
        bullet_y += step_y
        bullet_circle = bullet_surf.get_rect(center=(bullet_x, int(bullet_y)))
        screen.blit(surface, (0, 0))
        screen.blit(bullet_surf, bullet_circle)
        pygame.display.update()
        clock.tick(my_tank01.bullet_speed)
        if step_x != 0:
            if last_y > bullet_y:
                step_y += 2 / diff_x
            else:
                step_y += 1.3 / diff_x
        new_x = bullet_x + 1
    # Если снаряд коснулся поверхности не в минимальной точке, то ломать землю
    if not (bullet_y < window_height - surface_heights[bullet_x] - settings01.up_ground):
        by = bullet_y
        for bx in range(bullet_x - 10, bullet_x - 3):
            if window_height - by >= 0:
                if surface_heights[bx] >= window_height - by - settings01.up_ground:
                    surface_heights[bx] = window_height - by - settings01.up_ground
            else:
                surface_heights[bx] = 0
            by += 1
        for bx in range(bullet_x - 3, bullet_x + 3):
            if window_height - by >= 0:
                if surface_heights[bx] >= window_height - by - settings01.up_ground:
                    surface_heights[bx] = window_height - by - settings01.up_ground
            else:
                surface_heights[bx] = 0
        for bx in range(bullet_x + 3, bullet_x + 10):
            if window_height - by >= 0:
                if surface_heights[bx] >= window_height - by - settings01.up_ground:
                    surface_heights[bx] = window_height - by - settings01.up_ground
            else:
                surface_heights[bx] = 0
            by -= 1
    if tank1_x <= bullet_x < tank1_x + 40:
        tank1_hp -= 10
    elif tank2_x <= bullet_x < tank2_x + 40:
        tank2_hp -= 10

    if (tank1_hp <= 0) or (tank2_hp <= 0):
        return 0


# Основная функция игры
def game():
    # global tanks_in_game
    global tank_check
    # global con
    # global cur
    global tank1_x
    global tank2_x
    global tank1_hp
    global tank2_hp
    global surface_heights
    global amplitude
    global frequency


    # Создание массива для хранения высот поверхности
    surface_heights = np.zeros((window_width,))

    # Заполнение массива синусоидными значениями
    amplitude = settings01.AMPLITUDE  # Амплитуда синусоиды
    frequency = settings01.FREQUENCY  # Частота синусоиды

    for i in range(window_width):
        surface_heights[i] = amplitude * np.sin(frequency * i) + amplitude + 50

    tank_check = 1

    tank1_x = random.randint(10, window_width // 2 - 50)
    tank1_hp = 100
    tank1 = Tank((tank1_x, 400))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(tank1)
    collision = tank1.have_center_collision(surface_heights)
    if collision[0]:
        tank1.move(
            0,
            collision[1] if collision[1] < -1 else 0,
            surface_heights
        )
    else:
        tank1.move(0, collision[1], surface_heights)

    tank2_x = random.randint(window_width // 2 + 10, window_width - 50)
    tank2_hp = 100
    tank2 = Tank((tank2_x, 400))
    all_sprites.add(tank2)
    pygame.display.flip()
    collision = tank2.have_center_collision(surface_heights)
    if collision[0]:
        tank2.move(
            0,
            collision[1] if collision[1] < -1 else 0,
            surface_heights
        )
    else:
        tank2.move(0, collision[1], surface_heights)

    # for t in range(len(tanks_in_game)):
    #     x = cur.execute('select x_coord from base_in_game where tank = ?', (tanks_in_game[t][0],)).fetchall()
    #     y = cur.execute('select y_coord from base_in_game where tank = ?', (tanks_in_game[t][0],)).fetchall()
    #     new_tank = Tank((x, y))
    #     tanks_in_game[t][1] = new_tank

    font = pygame.font.SysFont('Comic Sans MS', 30)

    battle = True
    running = True
    while running:
        if battle:
            if tank_check > tank_count:
                tank_check = 1
            # tank = tanks_in_game[tank_check][1]
            if tank_check == 1:
                tank = tank1
            else:
                tank = tank2
            for event in pygame.event.get():  # обработка нажатия на крестик (выход)
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if shot(tank, int(mouse_x), int(mouse_y)) == 0:
                            battle = False
                        print(tank1_hp)
                        print(tank2_hp)
                        tank_check += 1
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                tank.move(tank_speed, 0, surface_heights)
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                tank.move(-tank_speed, 0, surface_heights)

            if tank_check == 1:
                tank1_x = tank.tanks_x()
            else:
                tank2_x = tank.tanks_x()

            collision = tank.have_center_collision(surface_heights)
            if collision[0]:
                tank.move(
                    0,
                    collision[1] if collision[1] < -1 else 0,
                    surface_heights
                )
            else:
                tank.move(0, collision[1], surface_heights)

            # surface.fill((sky_r, sky_g, sky_b))
            surface.fill(settings01.sky)

            for x in range(window_width):
                y = int(surface_heights[x])
                # pygame.draw.line(surface, (ground_r, ground_g, ground_b), (x, height), (x, height - y))
                pygame.draw.line(surface, settings01.ground, (x, window_height), (x, window_height - y - 9))

            all_sprites.update()
            all_sprites.draw(surface)
            # tank.draw(surface)

            screen.blit(surface, (0, 0))

            player1_hp_rect = pygame.Rect(25, 25, 310, 50)
            player1_hp = pygame.Rect(30, 30, tank1_hp * step_hp_rect, 40)
            player1_not_hp = pygame.Rect(30, 30, 300, 40)
            pygame.draw.rect(screen, 'black', player1_hp_rect, border_radius=5)
            pygame.draw.rect(screen, 'red', player1_not_hp)
            pygame.draw.rect(screen, 'green', player1_hp)

            player2_hp_rect = pygame.Rect(window_width - (25 + 310), 25, 310, 50)
            player2_hp = pygame.Rect(window_width - (30 + 300), 30, tank2_hp * step_hp_rect, 40)
            player2_not_hp = pygame.Rect(window_width - (30 + 300), 30, 300, 40)
            pygame.draw.rect(screen, 'black', player2_hp_rect, border_radius=5)
            pygame.draw.rect(screen, 'red', player2_not_hp)
            pygame.draw.rect(screen, 'green', player2_hp)

            pygame.display.flip()
            # clock.tick(FPS)
        else:
            if tank1_hp <= 0:
                win = 'Player 2 win!'
            else:
                win = 'Player 1 win!'
            final_screen(win)


if __name__ == '__main__':
    screen.fill(pygame.Color("black"))
    pygame.display.flip()
    screen.set_alpha(None)
    clock = pygame.time.Clock()
    start_screen()

    exit()
