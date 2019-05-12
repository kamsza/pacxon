import pygame
import tilemap
from moving_objects import MovingObject


class Pacman(MovingObject):
    def __init__(self):
        super().__init__('images/pacman_prawo.png')
        self.x = 0
        self.y = 0
        self.speed = 4
        self.marked_tiles = []

    def check_move(self):
        x_ind = tilemap.row_num(self.x + self.width / 2)
        y_ind = tilemap.col_num(self.y + self.height / 2)

        key = pygame.key.get_pressed()

        # pacman can stop only if is on occupied tile
        if tilemap.tile_map[y_ind][x_ind]:
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
        if tilemap.tile_map[y_ind][x_ind] == 2:
            if y_ind == 0:
                self.y_vec = max(0, self.y_vec)
            elif y_ind == tilemap.height - 1:
                self.y_vec = min(0, self.y_vec)
            if x_ind == 0:
                self.x_vec = max(0, self.x_vec)
            elif x_ind == tilemap.width - 1:
                self.x_vec = min(0, self.x_vec)

    # jedna z opcji zaznaczania śladu pacmana
        self.mark_tile(x_ind, y_ind)

    def mark_tile(self, x_ind, y_ind):
        if tilemap.tile_map[y_ind][x_ind] == 0:
            tilemap.tile_map[y_ind][x_ind] = 3
            self.marked_tiles.append((x_ind, y_ind))
        elif self.marked_tiles:
            tilemap.mark_area()
            for (x, y) in self.marked_tiles:
                if tilemap.tile_map[y][x] == 3:  # ten if wyleci - uderzenie duszka ma zabić pacmana
                    tilemap.tile_map[y][x] = 1
                self.marked_tiles.remove((x, y))
