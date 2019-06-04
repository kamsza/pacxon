import tilemap
import ghost
import pacman
import stats
import control
import not_moving_objects


player = None
objects = list()

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

    not_moving_objects.start_fruit_thread()


def action():
    player.action()

    for o in objects:
        o.action()


def add_orange_ghost(pos):
    global orange_ghosts_num

    if orange_ghosts_num > 0:
        y_ind, x_ind = pos[0]
        if tilemap.tile_map[y_ind][x_ind] != 1:
            return
        objects.append(ghost.OrangeGhost(x_ind, y_ind))
        orange_ghosts_num -= 1


def add_fruit(fruit):
    fruits.append(fruit)

def check_win_decorator(function):
    def wrapper():
        func = function()

        if round(100 * tilemap.marked_fields / tilemap.MAP_FIELDS) > 80:
            player.reset_position()
            control.win()
        else:
            return func
    return wrapper


def check_loss_decorator(function):
    def wrapper():
        func = function()

        if stats.player_lives == 0:
            control.game_over()
            stats.player_lives = stats.lives
            player.reset_position()
            print("LOSS")
        else:
            return func
    return wrapper


@check_loss_decorator
def kill_player():
    player.reset_position()
    stats.player_lives -= 1

def clear():
    global player, objects, orange_ghosts_num
    player = None
    del objects[:]


def set_pacman_speed(speed):
    player.set_speed(speed)

def set_ghost_speed(speed):
    for o in objects:
        o.set_speed(speed)
