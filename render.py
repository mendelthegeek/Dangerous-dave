from banner import *
from player import *
from tiles import *

board = pygame.display.set_mode((640, 392))

def init_tiles(tiles, gems, doors):
    gem_list = [
        ("blue_gem", (1, 6)),
        ("blue_gem", (7, 6)),
        ("blue_gem", (1, 4)),
        ("blue_gem", (5, 4)),
        ("blue_gem", (9, 4)),
        ("blue_gem", (13, 4)),
        ("blue_gem", (17, 4)),
        ("blue_gem", (3, 2)),
        ("blue_gem", (7, 2)),
        ("blue_gem", (15, 2)),
        ("red_gem", (17, 1)),
        ("purple_gem", (1, 1)),
    ]
    tiles.create_tile("horizontal_pipe", (1, 8))
    for i in range(4):
        tiles.create_tile("red_brick", (3 + i * 4, 3))
    for i in range(5):
        tiles.create_tile("red_brick", (1 + i * 4, 5))
    for i in range(4):
        tiles.create_tile("red_brick", (4 + i, 7))
    for i in range(6):
        tiles.create_tile("red_brick", (11 + i, 7))
    tiles.create_tile("red_brick", (11, 8))
    board.blit(*doors.create_tile((12, 8)))

    for j in range(10):
        tiles.create_tile("red_brick", (0, j))
    for j in range(10):
        tiles.create_tile("red_brick", (19, j))
    for j in range(10):
        tiles.create_tile("red_brick", (18, j))
    for i in range(20):
        tiles.create_tile("red_brick", (i, 0))
    for i in range(20):
        tiles.create_tile("red_brick", (i, 9))

    trophy = Trophy((352, 106))
    gems.add(trophy)
    for gem_info in gem_list:
        board.blit(*gems.create_tile(*gem_info))


def render(dave, tiles, gems, doors, curr_score):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    for tile in tiles.sprites():
        board.blit(tile.image, tile.rect)
    for door in doors.sprites():
        board.blit(door.image, door.rect)
    for gem in gems.sprites():
        if gem.gem_type == "trophy":
            board.blit(*gem.get_image())
        else:
            board.blit(gem.image, gems.unpad(gem.rect))
    if current_time - dave.last_update > dave.speed:
        dave.move()
        dave.last_update = current_time
    board.blit(dave.current_display(), dave.position())
    if dave.has_key:
        board.blit(go_thru(), (180, 358))
    blit_border(board, curr_score)
    pygame.display.flip()
