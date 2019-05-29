import pygame
import tilemap_view
import time

done = False
f = "default_tile_map.txt"


def wait_for_keypress():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
            if event.type == pygame.KEYDOWN:
                return


def game_over():
    tilemap_view.game_over_view()
    wait_for_keypress()


def win():
    pass