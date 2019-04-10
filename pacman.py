import pygame
import tilemap
from random import choice
from abc import ABC, abstractmethod


class Pacman:
    def __init__(self):
        self.width = tilemap.tile_size
        self.height = tilemap.tile_size
        self.step = tilemap.tile_size
        self.img = pygame.image.load('images/pacman_prawo.png')
        self.img_width, self.img_height = self.img.get_rect().size
        self.x_vec = 1
        self.y_vec = 1
        self.x = tilemap.width // 2 * tilemap.tile_size
        self.y = tilemap.height // 2 * tilemap.tile_size
        # 12 divided by speed must give natural number

    def draw(self, screen):
        img_x = self.x + (tilemap.tile_size - self.img_width) / 2
        img_y = self.y + (tilemap.tile_size - self.img_height) / 2
        screen.blit(self.img, (img_x, img_y))

    def move(self, direction):
        self.check_move()

        self.x += self.step * direction[0] * self.x_vec
        self.y += self.step * direction[1] * self.x_vec

    def check_move(self):
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2

        x_ind = tilemap.row_num(center_x)
        y_ind = tilemap.col_num(center_y)
        # if x_ind > tilemap.width:
        #     self.x_vec = 0
        # elif x_ind == 0:
        #     self.x_vec = 0
        # else:
        #     self.x_vec = 1
        # if y_ind > tilemap.height:
        #     self.y_vec = 0
        # elif y_ind == 0:
        #     self.y_vec = 0
        # else:
        #     self.y_vec = 1



