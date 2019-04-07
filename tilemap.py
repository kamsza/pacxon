import pygame

textures = {
    1: pygame.image.load('images/occ.png'),
    0: pygame.image.load('images/free.png')
}

tile_size = 24
tile_map = []
width = 0
height = 0


def init(file):
    global tile_map, width, height
    tile_map = [[int(n) for n in line.split()] for line in open(file, "r")]
    width = len(tile_map[0])
    height = len(tile_map)


def draw(screen):
    for row in range(height):
        for column in range(width):
            screen.blit(textures[tile_map[row][column]], (column * tile_size, row * tile_size))


def row_num(x):
    return int(x / tile_size)


def col_num(y):
    return int(y / tile_size)
