import tilemap
import ghost
import pacman
import stats
import control
import not_moving_objects

player = None
objects = list()
#TODO lista na owoce

orange_ghosts_num = 0


def init():
    global orange_ghosts_num, player

    player = pacman.Pacman()

    for i in range(stats.blue_ghosts_num):
        objects.append(ghost.BlueGhost())

    for i in range(stats.red_ghosts_num):
        objects.append(ghost.RedGhost())

    for i in range(stats.green_ghosts_num):
        objects.append(ghost.GreenGhost())


    orange_ghosts_num = stats.orange_ghosts_num


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


def execute_fruit_action(number):
    for o in objects:
        o.fruit_action(number)


def end_fruit_action():
    for o in objects:
        o.reset_speed
    player.reset_speed


def kill_player():
    player.reset_position()
    stats.player_lives -= 1

    if stats.player_lives == 0:
        control.game_over()
        stats.player_lives = stats.lives


