import pygame
import ghost
import tilemap
import pacman

clock = pygame.time.Clock()
done = False

pygame.init()
tilemap.init("default_tile_map.txt")

tilemap.objects.append(pacman.Pacman())

tilemap.objects.append(ghost.BlueGhost())
#
# tilemap.objects.append(ghost.BlueGhost())
#
# tilemap.objects.append(ghost.BlueGhost())
#
# tilemap.objects.append(ghost.BlueGhost())
#
# tilemap.objects.append(ghost.RedGhost())
#
# tilemap.objects.append(ghost.GreenGhost())


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tilemap.draw()

    for o in tilemap.objects:
        o.action()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
