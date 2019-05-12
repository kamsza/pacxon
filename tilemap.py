import pygame
import numpy
from scipy.ndimage import label

textures = {
    3: pygame.image.load('images/marked.png'),
    2: pygame.image.load('images/occ.png'),
    1: pygame.image.load('images/occ.png'),
    0: pygame.image.load('images/free.png'),
    -1: pygame.image.load('images/free.png')
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


def mark_area():
    s = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]

    # get free tiles
    a = numpy.array(tile_map)
    labeled_array, num_features = label(a <= 0, structure=s)

    # if there are more than one closed areas
    if num_features > 1:
        # for each area
        for i in range(1, num_features + 1):
            a = list(zip(*numpy.where(labeled_array == i)))

            # is obstacle in this area
            is_obstacle = [True for (x, y) in a if tile_map[x][y] == -1]

            if not is_obstacle:
                for (x, y) in a:
                    tile_map[x][y] = 1
