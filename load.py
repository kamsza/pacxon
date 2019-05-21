import ghost
import tilemap
import pacman


def init():
    tilemap.init("default_tile_map.txt")

    tilemap.set_orange_ghost_number(3)

    tilemap.objects.append(pacman.Pacman())

    tilemap.objects.append(ghost.BlueGhost())

    # tilemap.objects.append(ghost.BlueGhost())
    #
    # tilemap.objects.append(ghost.BlueGhost())
    #
    # tilemap.objects.append(ghost.BlueGhost())
    #
    # tilemap.objects.append(ghost.RedGhost())
    #
    # tilemap.objects.append(ghost.GreenGhost())
