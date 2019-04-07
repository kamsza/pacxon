import pygame
import tilemap
from random import choice
from abc import ABC, abstractmethod


class Ghost(ABC):
    def __init__(self):
        self.width = tilemap.tile_size
        self.height = tilemap.tile_size
        self.speed = 2                                               # 12 divided by speed must give natural number

    def draw(self, screen):
        img_x = self.x + (tilemap.tile_size - self.img_width) / 2
        img_y = self.y + (tilemap.tile_size - self.img_height) / 2
        screen.blit(self.img, (img_x, img_y))

    def move(self):
        self.x += self.x_vec * self.speed
        self.y += self.y_vec * self.speed
        self.check_move()

    def check_move(self):
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2
        dist_to_center_x = abs(center_x % tilemap.tile_size - tilemap.tile_size / 2)
        dist_to_center_y = abs(center_y % tilemap.tile_size - tilemap.tile_size / 2)
        x_ind = tilemap.row_num(center_x)
        y_ind = tilemap.col_num(center_y)
        collides = False
        collisions = 0

        if dist_to_center_x < self.speed and dist_to_center_y < self.speed:
            collides = self.check_collision(x_ind, y_ind)
        while collides:
            if collisions == 4:
                pass                                                                             # todo
            collisions += 1
            collides = self.check_collision(x_ind, y_ind)

    @abstractmethod
    def check_collision(self, x_ind, y_ind):
        pass


class BlueGhost(Ghost):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('images/blue_ghost.png')
        self.img_width, self.img_height = self.img.get_rect().size
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])
        self.x = tilemap.width // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size  # for tests
        self.y = tilemap.height // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size
        # self.x = randint(3, tilemap.width - 4) * tilemap.tile_size + 0.5 * tilemap.tile_size    # default
        # self.y = randint(3, tilemap.height - 4) * tilemap.tile_size + 0.5 * tilemap.tile_size

    def check_collision(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind + self.x_vec]:
            self.x_vec = -self.x_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind]:
            self.y_vec = -self.y_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec]:
            self.x_vec = -self.x_vec
            self.y_vec = -self.y_vec
        else:
            return False
        return True


class RedGhost(Ghost):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('images/red_ghost.png')
        self.img_width, self.img_height = self.img.get_rect().size
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])
        self.x = tilemap.width // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size  # for tests
        self.y = tilemap.height // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size
        # self.x = randint(3, tilemap.width - 4) * tilemap.tile_size + 0.5 * tilemap.tile_size    # default
        # self.y = randint(3, tilemap.height - 4) * tilemap.tile_size + 0.5 * tilemap.tile_size

    def check_collision(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind + self.x_vec]:
            if x_ind + self.x_vec != 0 and x_ind + self.x_vec != tilemap.width - 1:
                tilemap.tile_map[y_ind][x_ind + self.x_vec] = 0
            self.x_vec = -self.x_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind]:
            if y_ind + self.y_vec != 0 and y_ind + self.y_vec != tilemap.height - 1:
                tilemap.tile_map[y_ind + self.y_vec][x_ind] = 0
            self.y_vec = -self.y_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec]:
            if x_ind + self.x_vec != 0 and x_ind + self.x_vec != tilemap.width - 1:
                if y_ind + self.y_vec != 0 and y_ind + self.y_vec != tilemap.height - 1:
                    tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] = 0
            self.x_vec = -self.x_vec
            self.y_vec = -self.y_vec
        else:
            return False
        return True


# class GreenGhost(Ghost):
#     def __init__(self):
#         super().__init__()
#         self.img = pygame.image.load('images/green_ghost.png')
#         self.img_width, self.img_height = self.img.get_rect().size
#         self.x_vec = -1
#         self.y_vec = 0
#         self.x = (tilemap.width - 2) * tilemap.tile_size + 0.5 * tilemap.tile_size
#         self.y = (tilemap.height - 2) * tilemap.tile_size + 0.5 * tilemap.tile_size
#
#     def check_collision(self, x_ind, y_ind):
#         if tilemap.tile_map[y_ind][x_ind + self.x_vec]:
#             self.y_vec = self.x_vec
#             self.x_vec = 0
#         elif tilemap.tile_map[y_ind + self.y_vec][x_ind]:
#             self.x_vec = self.y_vec
#             self.y_vec = 0
#         elif tilemap.tile_map[y_ind + 1][x_ind] == 0 and tilemap.tile_map[y_ind + 1][x_ind - self.x_val]:
#             self.y_vec = 1
#             self.x_vec = 0
#         elif tilemap.tile_map[y_ind - 1][x_ind] == 0 and tilemap.tile_map[y_ind -1][x_ind - self.x_val]:
#             self.y_vec = 1
#             self.x_vec = 0
#         else:
#             return False
#         return True
