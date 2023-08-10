import pygame

import banner

BG = (50, 50, 50)

board = pygame.display.set_mode((640, 384))


def init_tiles(tiles, gems):
    gem_locs = [
        (100,200),
        (100,250),
        (300, 275)
    ]
    board.blit(*tiles.create_tile("horizontal_pipe", (32, 338)))
    for j in range(3):
        for i in range(7):
            board.blit(*tiles.create_tile("red_brick", (128 * (j + 1) + i * 32, 306 - j * 64)))
    for j in range(10):
        board.blit(*tiles.create_tile("red_brick", (0, 50 + j * 32)))
    for j in range(10):
        board.blit(*tiles.create_tile("red_brick", (608, 50 + j * 32)))
    for i in range(20):
        board.blit(*tiles.create_tile("red_brick", (i * 32, 50)))
    for i in range(20):
        board.blit(*tiles.create_tile("red_brick", (i * 32, 370)))
    for gem in gem_locs:
        board.blit(*gems.create_tile("blue_gem", gem))




def test_render(dave, tiles, gems, curr_score):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    if current_time - dave.last_update > dave.speed:
        dave.move()
        dave.last_update = current_time
    board.blit(dave.current_display(), dave.position())
    for tile in tiles.sprites():
        board.blit(tile.image, tile.rect)
    for gem in gems.sprites():
        if gem.gem_type == "trophy":
            board.blit(*gem.get_image())
        else:
            board.blit(gem.image, gem.rect)
    board.blit(banner.score(curr_score), (450, 10))
    pygame.display.flip()


