import tilemap
import ghost
import pacman
import stats
import control
import not_moving_objects
import threading
import time
from random import randint


player = None
objects = list()
green_fruits = list()
lemon_fruits = list()
sherry_fruits = list()
apple_fruits = list()

orange_ghosts_num = 0

once = True
t1, t2, t3, t4 = None, None, None, None


def init():
    global orange_ghosts_num, player, once

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


def kill_player():
    player.reset_position()
    stats.player_lives -= 1

    if stats.player_lives == 0:
        del_fruit_threads()
        control.game_over()
        stats.player_lives = stats.lives


def add_fruit():
    global once, t1, t2, t3, t4
    if once:
        t1 = threading.Thread(target=control_green)
        t1.start()
        t2 = threading.Thread(target=control_sherry)
        t2.start()
        t3 = threading.Thread(target=control_lemon)
        t3.start()
        t4 = threading.Thread(target=control_apple)
        t4.start()
        once = False


def del_fruit_threads():
    global t1, t2, t3, t4
    t1.join()
    t2.join()
    t3.join()
    t4.join()


def del_fruit(fruit):
    global objects
    tilemap.tile_map[fruit.y][fruit.x] = tilemap.tile_map[fruit.y][fruit.x - 1]


def control_green():
    time.sleep(randint(2, 10))
    while stats.green_fruit:
        fruit = not_moving_objects.Green()
        if fruit.taken == 0:
            fruit.action()
            time.sleep(10)
            del_fruit(fruit)
        time.sleep(5)


def control_sherry():
    time.sleep(randint(2, 10))
    while stats.sherry_fruit:
        fruit = not_moving_objects.Sherry()
        if fruit.taken == 0:
            fruit.action()
            time.sleep(10)
            del_fruit(fruit)
        time.sleep(5)


def control_apple():
    time.sleep(randint(2, 10))
    while stats.apple_fruit:
        fruit = not_moving_objects.Apple()
        if fruit.taken == 0:
            fruit.action()
            time.sleep(10)
            del_fruit(fruit)
        time.sleep(3)


def control_lemon():
    time.sleep(randint(2, 10))
    while stats.lemon_fruit:
        fruit = not_moving_objects.Lemon()
        if fruit.taken == 0:
            fruit.action()
            time.sleep(10)
            del_fruit(fruit)
        time.sleep(5)



