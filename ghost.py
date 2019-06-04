import pygame
import tilemap
import tilemap_objects
from random import choice, randint
from abc import ABC, abstractmethod
from moving_objects import MovingObject


# abstract class
class Ghost(MovingObject, ABC):
    def __init__(self, img):
        super().__init__(img)
        self.id = -1
        self.speed = 3
        self.x = randint(5, tilemap.WIDTH - 5) * tilemap.TILE_SIZE + 0.5 * tilemap.TILE_SIZE
        self.y = randint(5, tilemap.HEIGHT - 5) * tilemap.TILE_SIZE + 0.5 * tilemap.TILE_SIZE
        self.x_vec = choice([-1, 1])
        self.y_vec = choice([-1, 1])
        self.x_ind = tilemap.row_num(self.x)
        self.y_ind = tilemap.col_num(self.y)

    def check_move(self):
        x_ind = tilemap.row_num(self.x + self.img_width / 2)
        y_ind = tilemap.col_num(self.y + self.img_height / 2)
        self.update_position(x_ind, y_ind)

        collisions = 0
        collides = self.check_collision()
        while collides:
            self.handle_collision(collides)

            # if ghost is stuck - freeze him
            if collisions == 8:
                self.speed = 0
                self.img = pygame.image.load('images/frozen_ghost.png')
                collides = False
            else:
                collisions += 1
                collides = self.check_collision()

    def update_position(self, new_x, new_y):
        old_x, old_y = self.x_ind, self.y_ind
        tilemap.tile_map[old_y][old_x] = 0
        tilemap.tile_map[new_y][new_x] = self.id
        self.x_ind, self.y_ind = new_x, new_y

    def reset_speed(self):
        self.speed = 3

    @abstractmethod
    def check_collision(self):
        pass

    @abstractmethod
    def handle_collision(self, colliding_vec):
        pass

    @abstractmethod
    def fruit_action(self, number):
        pass


class BlueGhost(Ghost):
    def __init__(self, img='images/blue_ghost.png'):
        super().__init__(img)

    def check_collision(self):
        # next field horizontally
        if tilemap.tile_map[self.y_ind][self.x_ind + self.x_vec] > 0:
            return self.x_vec, 0
        # next field vertically
        elif tilemap.tile_map[self.y_ind + self.y_vec][self.x_ind] > 0:
            return 0, self.y_vec
        # next corner
        elif tilemap.tile_map[self.y_ind + self.y_vec][self.x_ind + self.x_vec] > 0:
            return self.x_vec, self.y_vec
        else:
            return ()

    def handle_collision(self, colliding_vec):
        x_col, y_col = colliding_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] in [1, 2]:
            # change moving direction
            if x_col:
                self.x_vec = -self.x_vec
            if y_col:
                self.y_vec = -self.y_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 3:
            tilemap_objects.kill_player()


    def fruit_action(self, number):
        if number == 11:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 12:
            self.speed = 1.5
        if number == 13:
            self.speed = 4
        if number == 14:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 0:
            tilemap.tile_map[self.y][self.x] = 0



class RedGhost(BlueGhost):
    def __init__(self):
        super().__init__('images/red_ghost.png')

    def handle_collision(self, colliding_vec):
        x_col, y_col = colliding_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 1:
            # change moving direction
            if x_col:
                self.x_vec = -self.x_vec
            if y_col:
                self.y_vec = -self.y_vec
            # destroy hit occupied tiles
            tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] = 0
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 2:
            # change moving direction
            if x_col:
                self.x_vec = -self.x_vec
            if y_col:
                self.y_vec = -self.y_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 3:
            tilemap_objects.kill_player()

    def fruit_action(self, number):
        if number == 11:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 12:
            self.speed = 4
        if number == 13:
            self.speed = 1.5
        if number == 14:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 0:
            tilemap.tile_map[self.y][self.x] = 0


class GreenGhost(Ghost):
    def __init__(self):
        super().__init__('images/green_ghost.png')
        self.x_ind = tilemap.WIDTH - 2
        self.y_ind = tilemap.HEIGHT - 2
        self.x_vec = choice([-1, 0])
        self.y_vec = 0 if self.x_vec else -1
        self.x = self.x_ind * tilemap.TILE_SIZE + self.x_vec * self.speed
        self.y = self.y_ind * tilemap.TILE_SIZE + self.y_vec * self.speed
        self.changed_dir = 0

        # moves along occupied fields
    def check_collision(self):
        if tilemap.tile_map[self.y_ind + self.y_vec][self.x_ind + self.x_vec] > 0:
            return self.x_vec, self.y_vec
        elif not self.changed_dir and tilemap.tile_map[self.y_ind - self.x_vec][self.x_ind + self.y_vec] == 0:
            return self.y_vec, -self.x_vec
        else:
            self.changed_dir = 0
            return ()

    def handle_collision(self, colliding_vec):
        x_col, y_col = colliding_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 0:
            # change moving direction
            if y_col:
                self.y_vec = -self.x_vec
                self.x_vec = 0
            if x_col:
                self.x_vec = self.y_vec
                self.y_vec = 0
            self.changed_dir = 1
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] in [1, 2]:
            # change moving direction
            if x_col:
                self.y_vec = self.x_vec
                self.x_vec = 0
            if y_col:
                self.x_vec = -self.y_vec
                self.y_vec = 0
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 3:
            tilemap_objects.kill_player()

    def fruit_action(self, number):
        if number == 11:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 12:
            self.speed = 4
        if number == 13:
            self.speed = 1.5
        if number == 14:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 0:
            tilemap.tile_map[self.y][self.x] = 0


class OrangeGhost(Ghost):
    def __init__(self, x_ind, y_ind):
        super().__init__('images/orange_ghost.png')
        self.id = 4
        self.x_ind = x_ind
        self.y_ind = y_ind
        self.x = x_ind * tilemap.TILE_SIZE + 0.5 * tilemap.TILE_SIZE
        self.y = y_ind * tilemap.TILE_SIZE + 0.5 * tilemap.TILE_SIZE

    # bounces off unoccupied fields and screen edges
    def check_collision(self):
        if tilemap.tile_map[self.y_ind][self.x_ind + self.x_vec] in [0, 2]:
            return self.x_vec, 0
        elif tilemap.tile_map[self.y_ind + self.y_vec][self.x_ind] in [0, 2]:
            return 0, self.y_vec
        elif tilemap.tile_map[self.y_ind + self.y_vec][self.x_ind + self.x_vec] in [0, 2]:
            return self.x_vec, self.y_vec
        else:
            return ()

    def handle_collision(self, colliding_vec):
        x_col, y_col = colliding_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] in [0, 2]:
            # change moving direction
            if x_col:
                self.x_vec = -self.x_vec
            if y_col:
                self.y_vec = -self.y_vec
        if tilemap.tile_map[self.y_ind + y_col][self.x_ind + x_col] == 3:
            tilemap_objects.kill_player()

    def fruit_action(self, number):
        if number == 11:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 12:
            self.speed = 1.5
        if number == 13:
            self.speed = 4
        if number == 14:
            self.speed = 0
            self.img = pygame.image.load('images/frozen_ghost.png')
        if number == 0:
            tilemap.tile_map[self.y][self.x] = 0

    def update_position(self, new_x, new_y):
        old_x, old_y = self.x_ind, self.y_ind
        tilemap.tile_map[old_y][old_x] = 1
        tilemap.tile_map[new_y][new_x] = self.id
        self.x_ind, self.y_ind = new_x, new_y
