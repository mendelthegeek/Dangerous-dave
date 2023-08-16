import sys

from banner import *
from player import *
from tiles import *
from render import *


class NextLevel:

    def __init__(self, curr_score):
        self.tiles = Tiles()
        self.doors = Door()
        for i in range(20):
            self.tiles.create_tile("blue_brick", (i, 3))
        self.doors.create_tile((0, 4))
        for i in range(20):
            self.tiles.create_tile("blue_brick", (i, 5))
        dave = Dave((32, 170))
        dave.x_speed = 1

        empty = pygame.sprite.Group()
        self.gems = empty
        self.hazards = empty
        self.run(dave, curr_score)

    def run(self, dave, curr_score):
        running = True
        while dave.x < 608 and running:
            render(dave, self, curr_score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

class Level1:

    def __init__(self):
        self.dave_pos = (64, 298)
        self.tiles = Tiles()
        self.gems = Gems()
        self.doors = Door()
        self.hazards = Hazards()
        self.doors.create_tile((12, 8))

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
        tile_list.append(("horizontal_pipe", (1, 8)))

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
        self.tiles.create_tile("horizontal_pipe", (1, 8))

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
            self.gems.create_tile(*gem)
        for tile in tile_list:
            self.tiles.create_tile(*tile)
        for i, hazard in enumerate(hazard_list):
            sprite = self.hazards.create_tile(*hazard)
            sprite.frame = i % len(sprite.images)
