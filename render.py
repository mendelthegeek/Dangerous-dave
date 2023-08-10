import pygame

import banner
from tiles import Trophy

BG = (50, 50, 50)

board = pygame.display.set_mode((640, 392))


def init_tiles(tiles, gems):
    board.blit(*tiles.create_tile("horizontal_pipe", (32, 330)))
    for j in range(3):
        for i in range(7):
            board.blit(*tiles.create_tile("red_brick", (128 * (j + 1) + i * 32, 298 - j * 64)))
    for j in range(10):
        board.blit(*tiles.create_tile("red_brick", (0, 42 + j * 32)))
    for j in range(10):
        board.blit(*tiles.create_tile("red_brick", (608, 42 + j * 32)))
    for i in range(20):
        board.blit(*tiles.create_tile("red_brick", (i * 32, 42)))
    for i in range(20):
        board.blit(*tiles.create_tile("red_brick", (i * 32, 362)))
    for i in range(18):
        for j in range(8):
            proposed = (32 + i*32, 74+j*32)
            if proposed not in [(tile.rect.left, tile.rect.top) for tile in tiles.sprites()]:
                board.blit(*gems.create_tile("red_gem", proposed))
    trophy = Trophy((576, 330))
    gems.add(trophy)




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
    board.blit(banner.score(curr_score), (450, 6))
    board.blit(pygame.image.load(r"resources/tileset/border.png"), (0, 32))
    empty_rect = (pygame.Surface((640, 14)))
    empty_rect.fill(BG)
    board.blit(empty_rect, (0, 378))
    board.blit(pygame.image.load(r"resources/tileset/border.png"), (0, 381))
    pygame.display.flip()


