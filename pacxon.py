import pygame
import numpy as np


clock = pygame.time.Clock()
done = False
start_map_file = open( "tailmap.txt", "r")
tile_map = [[int(n) for n in line.split()] for line in start_map_file]

textures = {
    1: pygame.image.load('occ.png'),
    0: pygame.image.load('free.png')
}

TILE_SIZE  = 25
MAP_WIDTH  = len(tile_map[0])
MAP_HEIGHT = len(tile_map)

pygame.init()
screen = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE,MAP_HEIGHT*TILE_SIZE))



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            screen.blit(textures[tile_map[row][column]], (column * TILE_SIZE, row * TILE_SIZE))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)