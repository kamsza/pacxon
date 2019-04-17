from ghost import *
import tilemap
import pacman

clock = pygame.time.Clock()
done = False

pygame.init()
tilemap.init("tests/tile_map_big.txt")
# tilemap.init("tilemap.txt")

ghosts = list()

ghosts.append(BlueGhost())

ghosts.append(RedGhost())

ghosts.append(GreenGhost())

ghosts.append(OrangeGhost())

pacman = pacman.Pacman()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tilemap.draw()

    for ghost in ghosts:
        ghost.action()

    pacman.action()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
