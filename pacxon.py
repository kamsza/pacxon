import pygame
from ghost import *
import tilemap
import pacman



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

ghosts.append(GreenGhost())

ghosts.append(OrangeGhost())
pacman1 = pacman.Pacman()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tilemap.draw(screen)

    for ghost in ghosts:
        ghost.draw(screen)
        ghost.move()
    key = pygame.key.get_pressed()
    direction = (0,0)
    if key[pygame.K_RIGHT]:
        direction = (1, 0)
        pacman1.img =  pygame.image.load('images/pacman_prawo.png')
    if key[pygame.K_LEFT]:
        direction = (-1, 0)
        pacman1.img = pygame.image.load('images/pacman_lewo.png')
    if key[pygame.K_DOWN]:
        direction = (0, 1)
        pacman1.img = pygame.image.load('images/pacman_dol.png')
    if key[pygame.K_UP]:
        direction = (0, -1)
        pacman1.img = pygame.image.load('images/pacman_gora.png')
    pacman1.draw(screen)
    pacman1.move(direction)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(20)
