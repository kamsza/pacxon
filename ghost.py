import pygame
import tilemap
from moving_objects import MovingObject
from random import choice
from abc import ABC, abstractmethod


class Ghost(MovingObject, ABC):
    def __init__(self, img):
        super().__init__(img)
        self.speed = 2

    def check_move(self):
        x_ind = tilemap.row_num(self.x + self.width / 2)
        y_ind = tilemap.col_num(self.y + self.height / 2)
        collisions = 0
        collides = self.check_collision(x_ind, y_ind)

        while collides:
            if collisions == 4:
                self.speed = 0
                self.img = pygame.image.load('images/frozen_ghost.png')
                collides = False
            else:
                collisions += 1
                collides = self.check_collision(x_ind, y_ind)

    @abstractmethod
    def check_collision(self, x_ind, y_ind):
        pass


class BlueGhost(Ghost):
    def __init__(self):
        super().__init__('images/blue_ghost.png')
        self.x = tilemap.width // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size  # for tests
        self.y = tilemap.height // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])

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
        super().__init__('images/red_ghost.png')
        self.x = tilemap.width // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size  # for tests
        self.y = tilemap.height // 2 * tilemap.tile_size + 0.5 * tilemap.tile_size
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])

    def check_collision(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind + self.x_vec]:
            if tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] != 2:
                tilemap.tile_map[y_ind][x_ind + self.x_vec] = 0
            self.x_vec = -self.x_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind]:
            if tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] != 2:
                tilemap.tile_map[y_ind + self.y_vec][x_ind] = 0
            self.y_vec = -self.y_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec]:
            if tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] != 2:
                tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] = 0
            self.x_vec = -self.x_vec
            self.y_vec = -self.y_vec
        else:
            return False
        return True


class GreenGhost(Ghost):
    def __init__(self):
        super().__init__('images/green_ghost.png')
        self.x_vec = -1
        self.y_vec = 0
        self.x = (tilemap.width - 2) * tilemap.tile_size
        self.y = (tilemap.height - 2) * tilemap.tile_size

    def check_collision(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind + self.x_vec]:
            self.y_vec = self.x_vec
            self.x_vec = 0
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind]:
            self.x_vec = -self.y_vec
            self.y_vec = 0
        elif self.x_vec and tilemap.tile_map[y_ind - self.x_vec][x_ind] == 0:
            self.y_vec = -self.x_vec
            self.x_vec = 0
            return False
        elif self.y_vec and tilemap.tile_map[y_ind][x_ind + self.y_vec] == 0:
            self.x_vec = self.y_vec
            self.y_vec = 0
            return False
        else:
            return False
        return True


class OrangeGhost(Ghost):
    def __init__(self):
        super().__init__('images/orange_ghost.png')
        self.x = (tilemap.width - 3) * tilemap.tile_size + 0.5 * tilemap.tile_size  # for tests
        self.y = 2 * tilemap.tile_size + 0.5 * tilemap.tile_size
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])

    def check_collision(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind + self.x_vec] in [0, 2]:
            self.x_vec = -self.x_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind] in [0, 2]:
            self.y_vec = -self.y_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] in [0, 2]:
            self.x_vec = -self.x_vec
            self.y_vec = -self.y_vec
        else:
            return False
        return True
