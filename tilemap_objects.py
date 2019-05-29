import tilemap
import ghost
import pacman

player = None
objects = list()

orange_ghosts_num = 0


def init(blue_ghosts, red_ghosts, green_ghosts, orange_ghosts):
    global orange_ghosts_num, player

    player = pacman.Pacman()

    for i in range(blue_ghosts):
        objects.append(ghost.BlueGhost())

    for i in range(red_ghosts):
        objects.append(ghost.RedGhost())

    for i in range(green_ghosts):
        objects.append(ghost.GreenGhost())

    orange_ghosts_num = orange_ghosts


def action():
    player.action()

    for o in objects:
        o.action()


def add_orange_ghost(x_ind, y_ind):
    global orange_ghosts_num
    if tilemap.tile_map[y_ind][x_ind] != 1:
        return
    objects.append(ghost.OrangeGhost(x_ind, y_ind))
    orange_ghosts_num -= 1

#
# player_lives = 5
# lives_now = 5
#
#
# def kill_player():
#     global lives_now
#
#     player.reset_position()
#     lives_now -= 1
#
#


