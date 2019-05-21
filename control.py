import pygame
import tilemap
import time
import load
import os

done = False


def wait_for_keypress():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False
            if event.type == pygame.KEYDOWN:
                return


def game_over():
    global done
    done = True

    tilemap.draw()
    for o in tilemap.objects:
        o.draw()

    # dim the background
    darken_val = 35
    dark = pygame.Surface((tilemap.width * tilemap.tile_size, tilemap.height* tilemap.tile_size), flags=pygame.SRCALPHA)
    dark.fill((darken_val, darken_val, darken_val))
    tilemap.screen.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    # write GAME OVER in the center
    font = pygame.font.SysFont("comicsansms", 72)
    font.set_bold(True)
    text = font.render("GAME OVER", True, (249, 166, 2))
    text_x = tilemap.width * tilemap.tile_size / 2 - text.get_rect().width / 2
    text_y = tilemap.height * tilemap.tile_size / 2 - text.get_rect().height / 2
    tilemap.screen.blit(text, (text_x, text_y))

    pygame.display.flip()
    pygame.display.update()

    time.sleep(1)

    wait_for_keypress()

    tilemap.clear()

    load.init()

    done = False


def win():
    global done
    done = True

    tilemap.draw()
    for o in tilemap.objects:
        o.draw()

    # dim the background
    darken_val = 35
    dark = pygame.Surface((tilemap.width * tilemap.tile_size, tilemap.height* tilemap.tile_size), flags=pygame.SRCALPHA)
    dark.fill((darken_val, darken_val, darken_val))
    tilemap.screen.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    # write GAME OVER in the center
    font = pygame.font.SysFont("comicsansms", 72)
    font.set_bold(True)
    text = font.render("YOU WON", True, (249, 166, 2))
    text_x = tilemap.width * tilemap.tile_size / 2 - text.get_rect().width / 2
    text_y = tilemap.height * tilemap.tile_size / 2 - text.get_rect().height / 2
    tilemap.screen.blit(text, (text_x, text_y))

    pygame.display.flip()
    pygame.display.update()

    time.sleep(1)

    wait_for_keypress()

    tilemap.clear()

    load.init()

    done = False
