from ghost import *
import tilemap
import pacman

clock = pygame.time.Clock()
done = False

pygame.init()
tilemap.init("tests/tile_map_big.txt")
#tilemap.init("tilemap.txt")

screen = pygame.display.set_mode((tilemap.width * tilemap.tile_size, tilemap.height * tilemap.tile_size))

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

    tilemap.draw(screen)

    for ghost in ghosts:
        ghost.draw(screen)
        ghost.move()

    pacman.draw(screen)
    pacman.move()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
