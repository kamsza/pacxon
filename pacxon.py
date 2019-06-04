import pygame
import tilemap
import control
import tilemap_view
import tilemap_objects
import not_moving_objects


clock = pygame.time.Clock()

pygame.init()

#tilemap.init_from_file("default_tile_map.txt")
tilemap.init(43, 28)
tilemap_objects.init()
a = 1
while not control.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tilemap_objects.del_fruit_threads()
            control.done = True

    tilemap_view.draw()

    tilemap_objects.action()
    tilemap_objects.add_fruit()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
