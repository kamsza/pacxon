import pygame
import tilemap
from random import choice
from random import randint
from abc import ABC, abstractmethod


class Ghost(ABC):
    def __init__(self):
        self.width = tilemap.tile_size
        self.height = tilemap.tile_size
        self.speed = 2

    def draw(self, screen):
        img_x = self.x + (tilemap.tile_size - self.img_width) / 2
        img_y = self.y + (tilemap.tile_size - self.img_height) / 2
        screen.blit(self.img, (img_x, img_y))

    def move(self):
        self.x += self.x_vec * self.speed
        self.y += self.y_vec * self.speed
        self.check_move()

    def check_move(self):
        x_ind = tilemap.row_num(self.x + self.width / 2)
        y_ind = tilemap.col_num(self.y + self.height / 2)
        collides = False
        collisions = 0

        if self.x % tilemap.tile_size == 0 and self.y % tilemap.tile_size == 0:
            collides = self.check_collision(x_ind, y_ind)
        while collides:
            if collisions == 4:
                self.speed = 0
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

    # def teleport(self):
    #     new_x = randint(4, tilemap.width - 5)
    #     new_y = randint(4, tilemap.height - 5)
    #     print(new_x, "  ", new_y)
    #     for i, j in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    #         if tilemap.tile_map[new_y + i * self.y_vec][new_x + j * self.x_vec]:
    #             self.teleport()
    #     self.x = new_x * tilemap.tile_size
    #     self.y = new_y * tilemap.tile_size


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
        super().__init__()
        self.img = pygame.image.load('images/green_ghost.png')
        self.img_width, self.img_height = self.img.get_rect().size
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
        super().__init__()
        self.img = pygame.image.load('images/orange_ghost.png')
        self.img_width, self.img_height = self.img.get_rect().size
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])
        self.x = (tilemap.width - 3) * tilemap.tile_size + 0.5 * tilemap.tile_size  # for tests
        self.y = 2 * tilemap.tile_size + 0.5 * tilemap.tile_size
        # self.x = randint(3, tilemap.width - 4) * tilemap.tile_size + 0.5 * tilemap.tile_size    # default
        # self.y = randint(3, tilemap.height - 4) * tilemap.tile_size + 0.5 * tilemap.tile_size

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
