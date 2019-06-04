import pygame
import tilemap
import control
import tilemap_view
import tilemap_objects
import stats
import not_moving_objects


clock = pygame.time.Clock()


pygame.init()

control.start_game()

while not control.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            not_moving_objects.end_fruit_thread()
            control.done = True
            quit()

    tilemap_view.draw()

    tilemap_objects.action()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
