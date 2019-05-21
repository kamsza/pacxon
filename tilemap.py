import ghost
import random
import pygame
import numpy
from scipy.ndimage import label

objects = list()

textures = {
    5: pygame.image.load('images/upper_bar.png'),   # statistics
    4: pygame.image.load('images/occ.png'),         # orange ghost
    3: pygame.image.load('images/marked.png'),      # pacman trace
    2: pygame.image.load('images/occ.png'),         # frame of a map
    1: pygame.image.load('images/occ.png'),         # occupied field
    0: pygame.image.load('images/free.png'),        # free field
    -1: pygame.image.load('images/free.png')        # blue / red / green ghost
}

tile_size = 24
tile_map = []
width = 0
height = 0
screen = None

orange_ghosts = 0


map_fields = 0
marked_fields = 0


def init(file):
    global tile_map, width, height, screen, map_fields
    tile_map = [[int(n) for n in line.split()] for line in open(file, "r")]
    width = len(tile_map[0])
    height = len(tile_map)
    map_fields = width * height - 2*(width + height) - width + 4
    screen = pygame.display.set_mode((width * tile_size, height * tile_size))


def draw():
    global screen
    for row in range(height):
        for column in range(width):
            screen.blit(textures[tile_map[row][column]], (column * tile_size, row * tile_size))
    draw_bar()


heart_red = pygame.image.load('images/heart.png')
heart_blue = pygame.image.load('images/heart_blue.png')
logo = pygame.image.load('images/logo.png')


def draw_bar():
    global map_fields, marked_fields, screen, width, tile_size, logo
    lives = objects[0].lives
    max_lives = objects[0].LIVES
    for l in range(0, lives):
        screen.blit(heart_red, (l * tile_size + 2, tile_size - 2))
    for l in range(lives, max_lives):
        screen.blit(heart_blue, (l * tile_size + 2, tile_size - 2))

    font = pygame.font.SysFont("comicsansms", 18)
    text = font.render(str(round(100 * marked_fields / map_fields)) + " %", True, (249, 166, 2))
    screen.blit(text, ((width - 2) * tile_size + 2, tile_size - 2))

    w, h = logo.get_size()
    screen.blit(logo, ((width / 2) * tile_size - w/2, 0))


def row_num(x):
    return int(x / tile_size)


def col_num(y):
    return int(y / tile_size)


def mark_path(path):
    global marked_fields, map_fields
    marked_fields += len(path)
    while path:
        (x, y) = path.pop()
        tile_map[y][x] = 1


def mark_area():
    global marked_fields, map_fields

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
                marked_fields += len(a)

                for (x, y) in a:
                    tile_map[x][y] = 1

                if orange_ghosts:
                    pos = random.sample(a, 1)
                    y, x = pos[0]
                    add_orange_ghost(x, y)


def add_orange_ghost(x_ind, y_ind):
    global orange_ghosts
    objects.append(ghost.OrangeGhost(x_ind, y_ind))
    orange_ghosts -= 1


def kill():
    objects[0].kill()


def end_game():
    print("THIS IS THE END")
