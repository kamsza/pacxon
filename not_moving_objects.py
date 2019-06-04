import pygame
import tilemap
from abc import ABC
from random import randint


# abstract class
class NotMovingObject(ABC):
    def __init__(self, number):
        self.width = tilemap.TILE_SIZE
        self.height = tilemap.TILE_SIZE
        self.x = randint(1, tilemap.WIDTH-1)
        self.y = randint(3, tilemap.HEIGHT-1)
        self.number = number
        self.taken = tilemap.tile_map[self.y][self.x]

    def draw(self):
        tilemap.tile_map[self.y][self.x] = self.number

    def action(self):
        self.draw()


class Lemon(NotMovingObject):

    def __init__(self, number=11):
        super().__init__(number)


class Green(NotMovingObject):

    def __init__(self, number=12):
        super().__init__(number)


class Sherry(NotMovingObject):

    def __init__(self, number=13):
        super().__init__(number)


class Apple(NotMovingObject):

    def __init__(self, number=14):
        super().__init__(number)
