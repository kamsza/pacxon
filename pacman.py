import pygame
import tilemap
from moving_objects import MovingObject


class Pacman(MovingObject):
    def __init__(self):
        super().__init__('images/pacman_prawo.png')
        self.x = tilemap.width // 2 * tilemap.tile_size
        self.y = tilemap.height // 2 * tilemap.tile_size
        self.speed = 4

    def check_move(self):
        key = pygame.key.get_pressed()
        direction = (0, 0)

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

        x_ind = tilemap.row_num(self.x + self.width / 2)
        y_ind = tilemap.col_num(self.y + self.height / 2)

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


