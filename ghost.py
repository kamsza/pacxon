import pygame
import tilemap
from moving_objects import MovingObject
from random import choice
from abc import ABC, abstractmethod


# abstract class
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
            # if ghost is stuck - freeze him
            if collisions == 4:
                self.speed = 0
                self.img = pygame.image.load('images/frozen_ghost.png')
                collides = False
            else:
                collisions += 1
                collides = self.check_collision(x_ind, y_ind)
        else:
            self.update_position(x_ind, y_ind)

    def update_position(self, x_ind, y_ind):
        (old_x, old_y) = self.position
        tilemap.tile_map[old_y][old_x] = 0
        tilemap.tile_map[y_ind][x_ind] = -1
        self.position = (x_ind, y_ind)

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
        self.position = (tilemap.row_num(self.x), tilemap.col_num(self.y))

    def check_collision(self, x_ind, y_ind):
        # next field horizontally
        if tilemap.tile_map[y_ind][x_ind + self.x_vec] > 0:
            self.x_vec = -self.x_vec
        # next field vertically
        if tilemap.tile_map[y_ind + self.y_vec][x_ind] > 0:
            self.y_vec = -self.y_vec
        # checking corner
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] > 0:
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
        self.position = (tilemap.row_num(self.x), tilemap.col_num(self.y))

    def check_collision(self, x_ind, y_ind):
        # same as in BlueGhost + can destroy hit occupied tiles
        if tilemap.tile_map[y_ind][x_ind + self.x_vec] > 0:
            if tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] != 2:
                tilemap.tile_map[y_ind][x_ind + self.x_vec] = 0
            self.x_vec = -self.x_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind] > 0:
            if tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] != 2:
                tilemap.tile_map[y_ind + self.y_vec][x_ind] = 0
            self.y_vec = -self.y_vec
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind + self.x_vec] > 0:
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
        self.position = (tilemap.row_num(self.x), tilemap.col_num(self.y))

    # moves along occupied fields
    def check_collision(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind + self.x_vec] > 0:
            self.y_vec = self.x_vec
            self.x_vec = 0
        elif tilemap.tile_map[y_ind + self.y_vec][x_ind] > 0:
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

    # bounces off unoccupied fields and screen edges
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

    def update_position(self, x_ind, y_ind):
        pass
