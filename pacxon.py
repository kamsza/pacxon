import pygame
import load
import tilemap
import control

clock = pygame.time.Clock()

pygame.init()

load.init()

while not control.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.done = True

    tilemap.draw()

    for o in tilemap.objects:
        o.action()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
