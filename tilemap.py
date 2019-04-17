import pygame

textures = {
    3: pygame.image.load('images/marked.png'),
    2: pygame.image.load('images/occ.png'),
    1: pygame.image.load('images/occ.png'),
    0: pygame.image.load('images/free.png')
}

tile_size = 24
tile_map = []
width = 0
height = 0
screen = None


def init(file):
    global tile_map, width, height, screen
    tile_map = [[int(n) for n in line.split()] for line in open(file, "r")]
    width = len(tile_map[0])
    height = len(tile_map)
    screen = pygame.display.set_mode((width * tile_size, height * tile_size))


def draw():
    global screen
    for row in range(height):
        for column in range(width):
            screen.blit(textures[tile_map[row][column]], (column * tile_size, row * tile_size))


def row_num(x):
    return int(x / tile_size)


def col_num(y):
    return int(y / tile_size)
