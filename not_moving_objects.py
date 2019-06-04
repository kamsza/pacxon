import pygame
import tilemap
from abc import ABC
from random import randint


# abstract class
class NotMovingObject(ABC):
    def __init__(self, img, number):
        self.width = tilemap.TILE_SIZE
        self.height = tilemap.TILE_SIZE
        self.img = pygame.image.load(img)
        self.img_width, self.img_height = self.img.get_rect().size
        self.x = randint(1, tilemap.WIDTH)
        self.y = randint(1, tilemap.HEIGHT)
        self.number = number

    def draw(self):
        img_x = self.x + (tilemap.TILE_SIZE - self.img_width) / 2
        img_y = self.y + (tilemap.TILE_SIZE - self.img_height) / 2
        tilemap.screen.blit(self.img, (img_x, img_y))
        tilemap.tile_map[self.y][self.x] = self.number

    def action(self):
        self.draw()


class Ntmo11(NotMovingObject):

    def __init__(self, img='images/wisnia.png', number=11):
        super().__init__(img, number)


class Ntmo12(NotMovingObject):

    def __init__(self, img='images/wisnia.png', number=12):
        super().__init__(img, number)


class Ntmo13(NotMovingObject):

    def __init__(self, img='images/wisnia.png', number=13):
        super().__init__(img, number)


class Ntmo14(NotMovingObject):

    def __init__(self, img='images/wisnia.png', number=14):
        super().__init__(img, number)


