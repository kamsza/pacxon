import pygame
import tilemap
import stats

textures = {
    14: pygame.image.load('images/apple_free.png'), # apple fruit
    13: pygame.image.load('images/sherry_free.png'), # sherry fruit
    12: pygame.image.load('images/green_free.png'), # green fruit
    11: pygame.image.load('images/lemon_free.png'), # lemon fruit
    5: pygame.image.load('images/upper_bar.png'),   # statistics
    4: pygame.image.load('images/occ.png'),         # orange ghost
    3: pygame.image.load('images/marked.png'),      # pacman trace
    2: pygame.image.load('images/occ.png'),         # frame of a map
    1: pygame.image.load('images/occ.png'),         # occupied field
    0: pygame.image.load('images/free.png'),        # free field
    -1: pygame.image.load('images/free.png')        # blue / red / green ghost
}


def draw():
    draw_map()
    draw_bar()


def draw_map():
    for row in range(tilemap.HEIGHT):
        for column in range(tilemap.WIDTH):
            tilemap.screen.blit(textures[tilemap.tile_map[row][column]], (column * tilemap.TILE_SIZE, row * tilemap.TILE_SIZE))
    draw_bar()


heart_red = pygame.image.load('images/heart.png')
heart_blue = pygame.image.load('images/heart_blue.png')
logo = pygame.image.load('images/logo.png')


def draw_bar():
    lives = stats.player_lives
    max_lives = stats.lives
    for l in range(0, lives):
        tilemap.screen.blit(heart_red, (l * tilemap.TILE_SIZE + 2, tilemap.TILE_SIZE - 2))
    for l in range(lives, max_lives):
        tilemap.screen.blit(heart_blue, (l * tilemap.TILE_SIZE + 2, tilemap.TILE_SIZE - 2))

    font = pygame.font.SysFont("comicsansms", 18)
    text = font.render(str(round(100 * tilemap.marked_fields / tilemap.MAP_FIELDS)) + " %", True, (249, 166, 2))
    tilemap.screen.blit(text, ((tilemap.WIDTH - 2) * tilemap.TILE_SIZE + 2, tilemap.TILE_SIZE - 2))

    w, h = logo.get_size()
    tilemap.screen.blit(logo, ((tilemap.WIDTH / 2) * tilemap.TILE_SIZE - w / 2, 0))


DARKEN_VAL = 35


def game_over_view():
    draw_map()
    draw_bar()

    # dim the background
    dark = pygame.Surface((tilemap.WIDTH * tilemap.TILE_SIZE, tilemap.HEIGHT * tilemap.TILE_SIZE),
                          flags=pygame.SRCALPHA)
    dark.fill((DARKEN_VAL, DARKEN_VAL, DARKEN_VAL))
    tilemap.screen.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    # write GAME OVER in the center
    font = pygame.font.SysFont("comicsansms", 72)
    font.set_bold(True)
    text = font.render("GAME OVER", True, (249, 166, 2))
    text_x = tilemap.WIDTH * tilemap.TILE_SIZE / 2 - text.get_rect().width / 2
    text_y = tilemap.HEIGHT * tilemap.TILE_SIZE / 2 - text.get_rect().height / 2
    tilemap.screen.blit(text, (text_x, text_y))

    pygame.display.update()
    pygame.display.flip()
