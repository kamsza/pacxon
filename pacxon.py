import pygame
from random import choice

clock = pygame.time.Clock()
done = False
start_map_file = open( "tailmap_for_tests.txt", "r")
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
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.speed = 0.2
        self.dx = self.speed * choice([-1,1])
        self.dy = self.speed * choice([-1,1])
        self.img = pygame.image.load('ghost.png')
        self.height, self.width = self.img.get_rect().size

    def draw(self):
        screen.blit(self.img, (self.x + 1, self.y))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.check_collision()

    def check_collision(self):
        center_x = (self.x + self.width/2)
        center_y = (self.y + self.height / 2)
        x_ind = int(center_x / tile_size)
        y_ind = int(center_y / tile_size)

        if abs(center_x % tile_size - tile_size / 2) <= self.speed:
            if tile_map[y_ind][x_ind + 1]:
                if self.dx > 0: self.dx = -self.dx
            elif tile_map[y_ind][x_ind - 1]:
                if self.dx < 0: self.dx = -self.dx
        elif abs(center_y % tile_size - tile_size / 2) <= self.speed:
            if tile_map[y_ind - 1][x_ind]:
                if self.dy < 0: self.dy = -self.dy
            elif tile_map[y_ind + 1][x_ind]:
                if self.dy > 0: self.dy = -self.dy


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
ghosts = Ghost()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for row in range(map_height):
        for column in range(map_width):
            screen.blit(textures[tile_map[row][column]], (column * tile_size, row * tile_size))

    ghosts.draw()
    ghosts.move()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)