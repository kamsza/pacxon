import pygame
import tilemap
import control
import tilemap_objects
from moving_objects import MovingObject
import not_moving_objects


class Pacman(MovingObject):
    def __init__(self):
        super().__init__('images/pacman_prawo.png')
        self.speed = 6
        self.marked_tiles = []

    def check_move(self):
        x_ind = tilemap.row_num(self.x + self.img_width / 2)
        y_ind = tilemap.col_num(self.y + self.img_height / 2)
        self.update_position(x_ind, y_ind)

        key = pygame.key.get_pressed()

        # pacman can stop only if is on occupied tile
        if tilemap.tile_map[y_ind][x_ind] not in [0, 11, 12, 13, 14]:
            direction = (0, 0)
        else:
            direction = (self.x_vec, self.y_vec)

        if key[pygame.K_RIGHT]:
            direction = (1, 0)
            self.img = pygame.image.load('images/pacman_prawo.png')
        elif key[pygame.K_LEFT]:
            direction = (-1, 0)
            self.img = pygame.image.load('images/pacman_lewo.png')
        elif key[pygame.K_DOWN]:
            direction = (0, 1)
            self.img = pygame.image.load('images/pacman_dol.png')
        elif key[pygame.K_UP]:
            direction = (0, -1)
            self.img = pygame.image.load('images/pacman_gora.png')

        (self.x_vec, self.y_vec) = direction

        # ensures, that character stays inside the map
        if tilemap.tile_map[self.y_ind][self.x_ind] == 2:
            if y_ind == 2:
                self.y_vec = max(0, self.y_vec)
            elif y_ind == tilemap.HEIGHT - 1:
                self.y_vec = min(0, self.y_vec)
            if x_ind == 0:
                self.x_vec = max(0, self.x_vec)
            elif x_ind == tilemap.WIDTH - 1:
                self.x_vec = min(0, self.x_vec)

        # pacman got a fruit
        if tilemap.tile_map[self.y_ind][self.x_ind] in [11, 12, 13, 14]:
            not_moving_objects.fruit_action(tilemap.tile_map[self.y_ind][self.x_ind])

        # marks pacman path
        self.mark_tile(x_ind, y_ind)

    def mark_tile(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind] in [0, 11, 12, 13, 14]:
            tilemap.tile_map[y_ind][x_ind] = 3
            self.marked_tiles.append((x_ind, y_ind))
        elif self.marked_tiles:
            tilemap.mark_area()
            tilemap.mark_path(self.marked_tiles.copy())
            del self.marked_tiles[:]

    def update_position(self, new_x, new_y):
        if tilemap.tile_map[new_y][new_x] in [-1, 3, 4]:
            tilemap_objects.kill_player()
        else:
            self.x_ind, self.y_ind = new_x, new_y

    def reset_position(self):
        self.x_ind = 0
        self.y_ind = 2

        self.x = self.x_ind * tilemap.TILE_SIZE
        self.y = self.y_ind * tilemap.TILE_SIZE

        self.x_vec = 0
        self.y_vec = 0

        path = self.marked_tiles.copy()
        del self.marked_tiles[:]
        while path:
            (x, y) = path.pop()
            tilemap.tile_map[y][x] = 0
