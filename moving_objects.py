import pygame
import tilemap
from abc import ABC, abstractmethod


# abstract class
class MovingObject(ABC):
    def __init__(self, img):
        self.x_ind = 0
        self.y_ind = 2
        self.x = self.x_ind * tilemap.TILE_SIZE
        self.y = self.y_ind * tilemap.TILE_SIZE
        self.x_vec = 0
        self.y_vec = 0
        self.speed = 0
        self.img = pygame.image.load(img)
        self.img_width, self.img_height = self.img.get_rect().size

    def draw(self):
        img_x = self.x + (tilemap.TILE_SIZE - self.img_width) / 2
        img_y = self.y + (tilemap.TILE_SIZE - self.img_height) / 2
        tilemap.screen.blit(self.img, (img_x, img_y))

    def move(self):
        # check_move() is used only if object is in the middle of a tile
        if self.x % tilemap.TILE_SIZE == 0 and self.y % tilemap.TILE_SIZE == 0:
            self.check_move()
        self.x += self.speed * self.x_vec
        self.y += self.speed * self.y_vec

    @abstractmethod
    def check_move(self):
        pass

    def action(self):
        self.move()
        self.draw()
