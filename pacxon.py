import pygame
import tilemap
import control
import tilemap_view
import tilemap_objects
import stats

clock = pygame.time.Clock()

pygame.init()

control.start_game()

while not control.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control.done = True

    tilemap_view.draw()

    tilemap_objects.action()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
