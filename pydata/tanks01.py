import pygame
import math

from pydata import settings01
from pydata import my_tank01


class Tank(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        tank_image = pygame.image.load(my_tank01.tank_model)
        self.width, self.height = tank_image.get_rect().size
        self.original_image = pygame.transform.scale(tank_image, (self.width, self.height))
        self.image = self.original_image.copy()
        self.rect = pygame.Rect(*pos, self.width, self.height)
        self.angle = 0

    def update_size(self, scale_factor):
        self.rect.width = int(self.rect.width * scale_factor)
        self.rect.height = int(self.rect.height * scale_factor)

    def move(self, x, y, heights):
        if 0 < self.rect.x + x < settings01.WIDTH - self.width:
            self.rect.x += x
            self.rect.y += y
            left_y = settings01.HEIGHT - int(heights[self.rect.bottomleft[0] + int(self.width / 2 - 2)])
            right_y = settings01.HEIGHT - int(heights[self.rect.bottomright[0] - int(self.width / 2 - 2)])
            # print(int(self.width / 2 - 1))
            # print(self.rect.bottomleft[0] + (self.width / 2 - 1), self.rect.bottomright[0] - (self.width / 2 - 1))
            # print(left_y, right_y)
            if max(left_y, right_y) - min(left_y, right_y) <= my_tank01.cross:
                diff_left_y, diff_right_y = (
                    settings01.HEIGHT - self.rect.bottomleft[1] - heights[self.rect.bottomleft[0]],
                    settings01.HEIGHT - self.rect.bottomright[1] - heights[self.rect.bottomright[0]],
                )
                self.angle = math.degrees(math.atan((diff_left_y - diff_right_y) / self.image.get_rect().height))
                self.image = pygame.transform.rotate(self.original_image, self.angle)
            else:
                self.rect.x -= x
                self.rect.y -= y
            # print(self.rect.x, self.rect.y)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)

    def have_center_collision(self, heights):
        mid_bottom_point = self.rect.midbottom
        left_y, right_y = (
            settings01.HEIGHT - self.rect.bottomleft[1] - heights[self.rect.bottomleft[0]],
            settings01.HEIGHT - self.rect.bottomright[1] - heights[self.rect.bottomright[0]],
        )
        # print(abs(left_y - right_y) // 2)
        return (
            mid_bottom_point[1] + abs(left_y - right_y) // 2 >= settings01.HEIGHT - heights[mid_bottom_point[0]],
            settings01.HEIGHT - mid_bottom_point[1] - abs(left_y - right_y) // 2 - heights[mid_bottom_point[0]],
        )

    def have_collision(self, heights):
        left_bottom_point, right_bottom_point = self.rect.bottomleft, self.rect.bottomright
        return (
            left_bottom_point[1] >= settings01.HEIGHT - heights[left_bottom_point[0]],
            right_bottom_point[1] >= settings01.HEIGHT - heights[right_bottom_point[0]],
        )

    def tanks_bullet(self):
        return self.rect.center

    def tanks_x(self):
        return self.rect.bottomleft[0]
