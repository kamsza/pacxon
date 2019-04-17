import pygame
import tilemap
from abc import ABC, abstractmethod


# abstract class
class MovingObject(ABC):
    def __init__(self, img):
        self.width = tilemap.tile_size
        self.height = tilemap.tile_size
        self.img = pygame.image.load(img)
        self.img_width, self.img_height = self.img.get_rect().size
        self.x = 0
        self.y = 0
        self.x_vec = 0
        self.y_vec = 0
        self.speed = 0

    def draw(self):
        img_x = self.x + (tilemap.tile_size - self.img_width) / 2
        img_y = self.y + (tilemap.tile_size - self.img_height) / 2
        tilemap.screen.blit(self.img, (img_x, img_y))

    def move(self):
        # check_move() is used only if object is in the middle of a tile
        if self.x % tilemap.tile_size == 0 and self.y % tilemap.tile_size == 0:
            self.check_move()
        self.x += self.speed * self.x_vec
        self.y += self.speed * self.y_vec

    @abstractmethod
    def check_move(self):
        pass

    def action(self):
        self.move()
        self.draw()