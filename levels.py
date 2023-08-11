from banner import *
from player import *
from tiles import *
from render import *


def next_level(curr_score):
    tiles = Tiles()
    doors = Door()
    for i in range(20):
        tiles.create_tile("blue_brick", (i, 3))
    doors.create_tile((0, 4))
    for i in range(20):
        tiles.create_tile("blue_brick", (i, 5))
    dave = Dave((32, 170))
    dave.x_speed = 1

    while dave.x < 608:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        render(dave, tiles, pygame.sprite.Group(), doors, curr_score)
    return True


def level_1(tiles, gems, doors):
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


def level_1(tiles, gems, doors):
    tiles.create_tile("horizontal_pipe", (1, 8))
    doors.create_tile((12, 8))
    gems.add(Trophy((352, 106)))

    gem_list = [
        ("blue_gem", (1, 6)),
        ("blue_gem", (7, 6)),
        ("red_gem", (17, 1)),
        ("purple_gem", (1, 1)),
    ]
    for i in range(4):
        if not i == 2:
            gem_list.append(("blue_gem", (3 + i * 4, 2)))
    for i in range(5):
        gem_list.append(("blue_gem", (1 + 4 * i, 4)))

    tile_list = []
    for i in range(4):
        tile_list.append(("red_brick", (3 + i * 4, 3)))
    for i in range(5):
        tile_list.append(("red_brick", (1 + i * 4, 5)))
    for i in range(4):
        tile_list.append(("red_brick", (4 + i, 7)))
    for i in range(6):
        tile_list.append(("red_brick", (11 + i, 7)))
    tile_list.append(("red_brick", (11, 8)))

    for j in range(10):
        tile_list.append(("red_brick", (0, j)))
    for j in range(10):
        tile_list.append(("red_brick", (19, j)))
    for j in range(10):
        tile_list.append(("red_brick", (18, j)))
    for i in range(20):
        tile_list.append(("red_brick", (i, 0)))
    for i in range(20):
        tile_list.append(("red_brick", (i, 9)))

    for tile in tile_list:
        tiles.create_tile(*tile)
    for gem in gem_list:
        gems.create_tile(*gem)
