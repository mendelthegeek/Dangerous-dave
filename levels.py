import sys

from banner import *
from player import *
from tiles import *
from render import *


class NextLevel:

    def __init__(self):
        self.dave_pos = (32, 170)
        self.tiles = Tiles()
        self.doors = Door()
        for i in range(20):
            self.tiles.create_tile("blue_brick", (i, 3))
        self.doors.create_tile((0, 4))
        for i in range(20):
            self.tiles.create_tile("blue_brick", (i, 5))

        self.level = self

        empty = pygame.sprite.Group()
        self.gems = empty
        self.hazards = empty


class Level1:

    def __init__(self):
        self.dave_pos = (64, 298)
        self.tiles = Tiles()
        self.gems = Gems()
        self.doors = Door()
        self.hazards = Hazards()
        self.door_start = (12, 8)
        self.doors.create_tile(self.door_start)

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

        tile_list = [("horizontal_pipe", (1, 8)), ("red_brick", (11, 8))]
        for i in range(4):
            tile_list.append(("red_brick", (3 + i * 4, 3)))
        for i in range(5):
            tile_list.append(("red_brick", (1 + i * 4, 5)))
        for i in range(4):
            tile_list.append(("red_brick", (4 + i, 7)))
        for i in range(6):
            tile_list.append(("red_brick", (11 + i, 7)))

        for i in range(20):
            tile_list.append(("red_brick", (i, 0)))
        for i in range(20):
            tile_list.append(("red_brick", (i, 9)))
        for j in range(10):
            tile_list.append(("red_brick", (0, j)))
        for j in range(10):
            tile_list.append(("red_brick", (18, j)))
        for j in range(10):
            tile_list.append(("dirt", (19, j)))

        for tile in tile_list:
            self.tiles.create_tile(*tile)
        for gem in gem_list:
            self.gems.create_tile(*gem)


class Level2:

    def __init__(self):
        self.dave_pos = (64, 298)
        self.tiles = Tiles()
        self.gems = Gems()
        self.doors = Door()
        self.hazards = Hazards()
        self.door_start = (48, 1)
        self.doors.create_tile(self.door_start)

        gem_list = [
            ("trophy", (13, 5)),
            ("blue_gem", (10, 8)),
            ("blue_gem", (7, 1)),
            ("red_gem", (1, 1)),
            ("red_gem", (8, 7)),
            ("purple_gem", (21, 1)),
            ("purple_gem", (28, 8)),
            ("purple_gem", (29, 5)),
            ("purple_gem", (32, 8)),
            ("purple_gem", (37, 8))
        ]
        for i in range(6):
            gem_list.append(("blue_gem", (16 + i, 7)))

        tile_list = [("horizontal_pipe", (1, 8))]
        for j in range(10):
            tile_list.append(("red_brick", (0, j)))
        for j in range(5):
            tile_list.append(("red_brick", (9, j + 5)))
        for j in range(6):
            tile_list.append(("red_brick", (14, j + 4)))
        for j in range(5):
            tile_list.append(("red_brick", (23, j + 4)))
        for i in range(51):
            tile_list.append(("red_brick", (i, 0)))
        for i in range(5):
            tile_list.append(("red_brick", (i + 25, 2)))
        for i in range(9):
            tile_list.append(("red_brick", (i + 27, 4)))
        for j in range(3):
            tile_list.append(("red_brick", (30, j + 5)))
        for j in range(3):
            tile_list.append(("red_brick", (31, j + 1)))
        for j in range(3):
            tile_list.append(("red_brick", (32, j + 1)))
        for j in range(3):
            tile_list.append(("red_brick", (33, j + 6)))
        for j in range(6):
            tile_list.append(("red_brick", (38, j + 3)))
        for i in range(3):
            tile_list.append(("red_brick", (i, 9)))
        for i in range(16):
            tile_list.append(("red_brick", (i+23, 9)))
        for i in range(17):
            tile_list.append(("red_brick", (34 + i, 2)))
        for i in range(3):
            tile_list.append(("purple_horizontal", (i + 4, 7)))
        for i in range(3):
            tile_list.append(("purple_horizontal", (i + 8, 4)))
        for i in range(6):
            tile_list.append(("purple_horizontal", (16 + i, 5)))
        purple_horizontal_singles = [(1, 3), (4, 3), (2, 5), (3, 5), (13, 3), (11, 6), (13, 8)]
        for location in purple_horizontal_singles:
            tile_list.append(("purple_horizontal", location))
        red_brick_singles = [(24, 4), (24, 3), (25, 3), (25, 6), (25, 7), (26, 5), (27, 5), (27, 7),
                             (27, 8), (28, 7), (32, 7), (35, 5), (35, 6), (36, 8), (37, 6), (49, 1),
                             (50, 1)]
        for location in red_brick_singles:
            tile_list.append(("red_brick", location))

        hazard_list = []
        for i in range(6):
            hazard_list.append(("fire", (i + 3, 9)))
        for i in range(4):
            hazard_list.append(("fire", (i + 10, 9)))
        for i in range(8):
            hazard_list.append(("water", (i + 15, 9)))
        for i in range(12):
            hazard_list.append(("fire", (i + 39, 9)))
        for j in range(5):
            hazard_list.append(("purple_fire", (39, j + 3)))
        for j in range(5):
            hazard_list.append(("purple_fire", (41, j + 3)))
        for j in range(5):
            hazard_list.append(("purple_fire", (43, j + 3)))
        for j in range(3):
            hazard_list.append(("purple_fire", (47, j + 4)))
        purple_fires = [(40, 3), (40, 5), (44, 3), (44, 5), (44, 7), (48, 3), (49, 3), (48, 7), (49, 7),
                        (45, 4), (45, 6)]
        for location in purple_fires:
            hazard_list.append(("purple_fire", location))

        for gem in gem_list:
            self.gems.create_tile(*gem)
        for tile in tile_list:
            self.tiles.create_tile(*tile)
        for i, hazard in enumerate(hazard_list):
            sprite = self.hazards.create_tile(*hazard)
            sprite.frame = i % len(sprite.images)
