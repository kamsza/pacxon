import pygame
import tilemap_view
import time
import stats
import time
import tilemap
import tilemap_objects


done = False
f = "default_tile_map.txt"


def level_up():
    stats.this_level += 1
    stats.load_from_file()

def wait_for_keypress():
    wait = True
    time.sleep(.5)
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
            if event.type == pygame.KEYDOWN:
                return


def game_over():
    tilemap_view.game_over_view()
    tilemap_view.clear()
    wait_for_keypress()


def win():
    level_up()
    tilemap_view.game_win_view()
    tilemap_view.clear()
    wait_for_keypress()

def start_game():
    tilemap.init(43, 28)

    start_level = tilemap_view.start_view()

    stats.load_from_file(level=start_level)

    tilemap_objects.init()

