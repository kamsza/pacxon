import pygame
from ghost import *
import tilemap


clock = pygame.time.Clock()
done = False

pygame.init()
tilemap.init("tests/tile_map_big.txt")
#tilemap.init("tilemap.txt")

screen = pygame.display.set_mode((tilemap.width * tilemap.tile_size, tilemap.height * tilemap.tile_size))
# screen = pygame.display.set_mode((400, 300))

# print((tilemap.width, tilemap.height))

ghosts = []

ghosts.append(BlueGhost())

ghosts.append(RedGhost())


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tilemap.draw(screen)

    for ghost in ghosts:
        ghost.draw(screen)
        ghost.move()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
