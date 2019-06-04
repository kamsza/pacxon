import pygame
import tilemap
from abc import ABC
import random
import threading
import time
import control
import tilemap_objects


thread_1 = None
thread_2 = None
thread_3 = None

ID_LIST = [11, 12, 13, 14]


def get_position():
    x = random.randint(3, tilemap.WIDTH - 3)
    y = random.randint(5, tilemap.HEIGHT - 5)

    while tilemap.tile_map[y][x]:
        x = random.randint(3, tilemap.WIDTH - 3)
        y = random.randint(5, tilemap.HEIGHT - 5)
    return x, y


def draw_on_a_map(x, y):
    id = random.choice(ID_LIST)
    tilemap.tile_map[y][x] = id

def erase_from_a_map(x, y):
    tilemap.tile_map[y][x] = tilemap.tile_map[y][x+1]

def control_fruit():
    while not control.done:
        time.sleep(random.randint(2, 10))
        x, y = get_position()
        draw_on_a_map(x, y)
        time.sleep(random.randint(4, 6))
        erase_from_a_map(x, y)


def start_fruit_thread():
    global thread_1, thread_2, thread_3
    thread_1 = threading.Thread(target=control_fruit)
    thread_1.start()
    thread_2 = threading.Thread(target=control_fruit)
    thread_2.start()
    thread_3 = threading.Thread(target=control_fruit)
    thread_3.start()


def end_fruit_thread():
    global thread_1, thread_2, thread_3
    thread.join()


def fruit_action(id):
    thread = threading.Thread(target=control_action, args=(id,))
    thread.start()


def control_action(id):
    if id == 11:
        tilemap_objects.set_pacman_speed(12)
    if id == 12:
        tilemap_objects.set_pacman_speed(12)
    if id == 13:
        tilemap_objects.set_ghost_speed(0)
    if id == 13:
        tilemap_objects.set_ghost_speed(0)

    time.sleep(5)

    tilemap_objects.set_pacman_speed(6)
    tilemap_objects.set_ghost_speed(3)
