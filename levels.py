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

    empty = pygame.sprite.Group()
    while dave.x < 608:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        render(dave, tiles, empty, empty, doors, curr_score)
    return True


def level_1(tiles, gems, doors):
    tiles.create_tile("horizontal_pipe", (1, 8))
    doors.create_tile((12, 8))

    gem_list = [
        ("trophy", (11, 2)),
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


def level_2(tiles, hazards, gems, doors):
    tiles.create_tile("horizontal_pipe", (1, 8))

    gem_list = [
        ("trophy", (13, 5)),
        ("blue_gem", (10, 8)),
        ("blue_gem", (5, 1)),
        ("red_gem", (1, 1)),
        ("red_gem", (8, 7)),
    ]

    tile_list = []
    for j in range(10):
        tile_list.append(("red_brick", (0, j)))
    for j in range(5):
        tile_list.append(("red_brick", (9, j+5)))
    for j in range(6):
        tile_list.append(("red_brick", (14, j+4)))
    for i in range(20):
        tile_list.append(("red_brick", (i, 0)))
    for i in range(3):
        tile_list.append(("red_brick", (i, 9)))
    for i in range(3):
        tile_list.append(("purple_horizontal", (i+4, 7)))
    for i in range(3):
        tile_list.append(("purple_horizontal", (i+8, 4)))
    purple_horizontal_singles = [(1,3), (4, 3), (2,5), (3, 5), (13, 3), (11, 6), (13, 8)]
    for location in purple_horizontal_singles:
        tile_list.append(("purple_horizontal", location))

    hazard_list = []
    for i in range(6):
        hazard_list.append(("fire", (i+3, 9)))
    for i in range(4):
        hazard_list.append(("fire", (i+10, 9)))
    for i in range(6):
        hazard_list.append(("water", (i+15, 9)))

    for gem in gem_list:
        gems.create_tile(*gem)
    for tile in tile_list:
        tiles.create_tile(*tile)
    for hazard in hazard_list:
        hazards.create_tile(*hazard)
