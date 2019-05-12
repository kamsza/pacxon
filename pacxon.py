from ghost import *
#import tilemap
from pacman import *
from moving_objects import *

clock = pygame.time.Clock()
done = False

pygame.init()
tilemap.init("tests/tile_map_big.txt")
#tilemap.init("tilemap.txt")

objects = list()

objects.append(BlueGhost())

objects.append(RedGhost())

objects.append(GreenGhost())

objects.append(OrangeGhost())

objects.append(Pacman())


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    tilemap.draw()

    for o in objects:
        o.action()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


def ghost_position():
    global objects
    pos = []

    for o in objects:
        if isinstance(o, Ghost):
            pos.append((tilemap.row_num(o.x), tilemap.col_num(o.y)))

    return pos
