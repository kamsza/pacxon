import pygame
from random import choice

clock = pygame.time.Clock()
done = False
start_map_file = open( "tailmap_for_tests_big.txt", "r")
tile_map = [[int(n) for n in line.split()] for line in start_map_file]

textures = {
    1: pygame.image.load('occ.png'),
    0: pygame.image.load('free.png')
}

tile_size = 25
map_width = len(tile_map[0])
map_height = len(tile_map)
screen_width = map_width * tile_size
screen_height = map_height * tile_size


class Ghost:
    def __init__(self):
        self.img = pygame.image.load('ghost.png')
        self.width, self.height = self.img.get_rect().size
        self.speed = 2.5                                                # 12.5 divided by speed must give natural number
        self.x = map_width // 2 * tile_size + 0.5 * tile_size
        self.y = map_height // 2 * tile_size + 0.5 * tile_size
        self.dx = self.speed * choice([-1, 1])
        self.dy = self.speed * choice([-1, 1])

    def draw(self):
        img_x = self.x + (tile_size - self.width) / 2
        img_y = self.y + (tile_size - self.height) / 2
        screen.blit(self.img, (img_x, img_y))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.check_collision()

    def check_collision(self):
        center_x = self.x + tile_size / 2
        center_y = self.y + tile_size / 2
        dist_to_center_x = abs(center_x % tile_size - tile_size / 2)
        dist_to_center_y = abs(center_y % tile_size - tile_size / 2)
        x_ind = int(center_x / tile_size)
        y_ind = int(center_y / tile_size)
        collides = False

        if dist_to_center_x < self.speed and dist_to_center_y < self.speed:
            collides = True
            if tile_map[y_ind - 1][x_ind] and self.dy < 0:
                    self.dy = -self.dy
            elif tile_map[y_ind + 1][x_ind] and self.dy > 0:
                    self.dy = -self.dy
            elif tile_map[y_ind][x_ind - 1] and self.dx < 0:
                    self.dx = -self.dx
            elif tile_map[y_ind][x_ind + 1] and self.dx > 0:
                    self.dx = -self.dx
            elif tile_map[y_ind - 1][x_ind + 1] and self.dx > 0 and self.dy < 0:
                    self.dx = -self.dx
                    self.dy = -self.dy
            elif tile_map[y_ind + 1][x_ind + 1] and self.dx > 0 and self.dy > 0:
                    self.dx = -self.dx
                    self.dy = -self.dy
            elif tile_map[y_ind + 1][x_ind - 1] and self.dx < 0 and self.dy > 0:
                    self.dx = -self.dx
                    self.dy = -self.dy
            elif tile_map[y_ind - 1][x_ind - 1] and self.dx < 0 and self.dy < 0:
                    self.dx = -self.dx
                    self.dy = -self.dy
            else:
                collides = False
        if collides:
            self.check_collision()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
ghosts = []
for i in range(0, 9):
    ghosts.append(Ghost())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for row in range(map_height):
        for column in range(map_width):
            screen.blit(textures[tile_map[row][column]], (column * tile_size, row * tile_size))

    for ghost in ghosts:
        ghost.draw()
        ghost.move()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)