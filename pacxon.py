import pygame
import tilemap
import control
import tilemap_view
import tilemap_objects


clock = pygame.time.Clock()

pygame.init()

#tilemap.init_from_file("default_tile_map.txt")
tilemap.init(43, 28)
tilemap_objects.init(4, 2, 1, 3)

while not control.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.done = True

    tilemap_view.draw()

    tilemap_objects.action()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
