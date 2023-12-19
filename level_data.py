from monster import *
from render import *
from tiles import Tiles, Gems, Door, Hazards

import random

level_items = {}
mobs = Mobs()

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




nn = None
example_level_board =  [[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,nn,11,11,11,11,nn,nn,nn,nn,nn,nn,nn,nn,11,11,11,11,nn,11],
                        [11,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,nn,11],
                        [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11]]

def map_level_board_to_list(level_board): 
    tile_list, gem_list = [], []
    type_index = {1: tile_list, 2: gem_list}
    index_map = {1: 'red_brick', 2: 'blue_brick'}
    for i, row in enumerate(level_board): 
        for j, col in enumerate(row): 
            if not col: continue 
            str_col = str(col)
            c, e = int(str_col[0]), int(str_col[1])
            type_index[c].append((index_map[(e)], (j, i)))
    return type_index[1]
    

tile_list = map_level_board_to_list(example_level_board)
print(*tile_list, sep = '\n')

level_items[1] =  {'dave_pos': (64, 298),
                    'tiles': Tiles(),
                    'gems': Gems(),
                    'climbable': Climbable(),
                    'doors': Door(),
                    'hazards': Hazards(),
                    'door_start': (12, 8),
                    'mobs': pygame.sprite.Group(),

                    'gem_list': gem_list,
                    'tile_list': tile_list}

""""level 2"""
  
gem_list = [
    ("trophy", (13, 5)),
    ("blue_gem", (10, 8)),
    ("blue_gem", (7, 1)),
    ("red_gem", (1, 1)),
    ("red_gem", (8, 7)),
    ("purple_gem", (20, 1)),
    ("purple_gem", (27, 8)),
    ("purple_gem", (28, 5)),
    ("purple_gem", (31, 8)),
    ("purple_gem", (36, 8))
]
for i in range(5):
    gem_list.append(("blue_gem", (16 + i, 7)))

tile_list = [("horizontal_pipe", (1, 8))]
for j in range(10):
    tile_list.append(("red_brick", (0, j)))
for j in range(5):
    tile_list.append(("red_brick", (9, j + 5)))
for j in range(6):
    tile_list.append(("red_brick", (14, j + 4)))
for j in range(5):
    tile_list.append(("red_brick", (22, j + 4)))
for i in range(50):
    tile_list.append(("red_brick", (i, 0)))
for i in range(5):
    tile_list.append(("red_brick", (i + 24, 2)))
for i in range(9):
    tile_list.append(("red_brick", (i + 26, 4)))
for j in range(3):
    tile_list.append(("red_brick", (29, j + 5)))
for j in range(3):
    tile_list.append(("red_brick", (30, j + 1)))
for j in range(3):
    tile_list.append(("red_brick", (31, j + 1)))
for j in range(3):
    tile_list.append(("red_brick", (32, j + 6)))
for j in range(6):
    tile_list.append(("red_brick", (37, j + 3)))
for i in range(3):
    tile_list.append(("red_brick", (i, 9)))
for i in range(16):
    tile_list.append(("red_brick", (i + 22, 9)))
for i in range(17):
    tile_list.append(("red_brick", (33 + i, 2)))
for i in range(3):
    tile_list.append(("purple_horizontal", (i + 4, 7)))
for i in range(3):
    tile_list.append(("purple_horizontal", (i + 8, 4)))
for i in range(5):
    tile_list.append(("purple_horizontal", (16 + i, 5)))
purple_horizontal_singles = [(1, 3), (4, 3), (2, 5), (3, 5), (13, 3), (11, 6), (13, 8)]
for location in purple_horizontal_singles:
    tile_list.append(("purple_horizontal", location))
red_brick_singles = [(23, 4), (23, 3), (24, 3), (24, 6), (24, 7), (25, 5), (26, 5), (26, 7),
                        (26, 8), (27, 7), (31, 7), (34, 5), (34, 6), (35, 8), (36, 6), (48, 1),
                        (49, 1)]
for location in red_brick_singles:
    tile_list.append(("red_brick", location))

hazard_list = []
for i in range(6):
    hazard_list.append(("fire", (i + 3, 9)))
for i in range(4):
    hazard_list.append(("fire", (i + 10, 9)))
for i in range(7):
    hazard_list.append(("water", (i + 15, 9)))
for i in range(12):
    hazard_list.append(("fire", (i + 38, 9)))
for j in range(5):
    hazard_list.append(("purple_fire", (38, j + 3)))
for j in range(5):
    hazard_list.append(("purple_fire", (40, j + 3)))
for j in range(5):
    hazard_list.append(("purple_fire", (42, j + 3)))
for j in range(3):
    hazard_list.append(("purple_fire", (46, j + 4)))
purple_fires = [(39, 3), (39, 5), (43, 3), (43, 5), (43, 7), (47, 3), (48, 3), (47, 7), (48, 7),
                (44, 4), (44, 6)]
for location in purple_fires:
    hazard_list.append(("purple_fire", location))


level_items[2] = {
    'hazard_list': hazard_list,
    'dave_pos': (64, 298),
    'tiles': Tiles(),
    'gems': Gems(),
    'climbable': Climbable(),
    'doors': Door(),
    'hazards': Hazards(),
    'door_start': (47, 1),
    'tile_list': tile_list,
    'gem_list': gem_list
    }


"""level 3"""

gem_list = [("jetpack", (66, 8)), ("trophy", (67, 8)), ("gun", (10, 3)), ("ring", (64, 1)),
                    ("wand", (71, 5)), ("crown", (71, 4)), ("wand", (72, 0)), ("wand", (74, 1))]
for i in range(4):
    gem_list.append(("wand", (76 + i * 3, 2)))
blue_gem_list = [1, 5, 14, 19, 23, 28, 52, 56]
for x in blue_gem_list:
    gem_list.append(("blue_gem", (x, 3)))

for i in range(3):
    gem_list.append(("blue_gem", (35 + i * 5, 3)))

tile_list = [("horizontal_pipe", (1, 5)), ("dirt", (63, 4)), ("dirt", (66, 4))]
dirt_list = [("ul", (72, 8)), ("ul", (73, 7)), ("ur", (70, 2)), ("ur", (75, 0)),
                ("ur", (76, 1)), ("ur", (85, 4))]
for i in range(3):
    dirt_list.append(("ll", (71 + i, i)))
for location in dirt_list:
    tile_list.append((f"dirt_{location[0]}", location[1]))

for j in range(10):
    tile_list.append(("dirt", (0, j)))
for j in range(10):
    tile_list.append(("dirt", (86, j)))
for i in range(71):
    tile_list.append(("dirt", (i, 0)))
for i in range(64):
    tile_list.append(("dirt", (i, 1)))
for i in range(63):
    tile_list.append(("dirt", (i, 7)))
for i in range(64):
    tile_list.append(("dirt", (i, 8)))
for i in range(71):
    tile_list.append(("dirt", (i, 9)))
for i in range(71, 87):
    tile_list.append(("dirt", (i, 3)))
for i in range(2):
    for j in range(2):
        tile_list.append(("dirt", (70 + i + j, j + 1)))
for i in range(76, 86):
    for j in range(2):
        tile_list.append(("dirt", (i + j, j)))
for j in range(3):
    for i in range(2):
        tile_list.append(("dirt", (72 + i - j, 6 + j)))
for j in [2, 6]:
    for i in range(1, 62):
        tile_list.append(("blue_pillar", (i, j)))

hazard_list = []
for i in range(3):
    hazard_list.append(("purple_fire", (5 + i * 4, 5)))
for i in range(5):
    hazard_list.append(("purple_fire", (19 + i * 4, 5)))
for i in range(3):
    hazard_list.append(("purple_fire", (36 + i * 4, 5)))
for j in range(3):
    for i in range(2):
        hazard_list.append(("fire", (62 + j + i * (9 - 2 * j), 6 + j)))
        hazard_list.append(("fire", (63 + j + i * (7 - 2 * j), 6 + j)))
for i in range(71, 84):
    hazard_list.append(("fire", (i, 9)))
purple_fires = [(14, 5), (47, 5), (52, 5), (53, 5)]
for location in purple_fires:
    hazard_list.append(("purple_fire", location))

level_items[3] = {
    'mobs': mobs,
    'hazard_list': hazard_list,
    'dave_pos': (64, 202),
    'tiles': Tiles(),
    'gems': Gems(),
    'climbable': Climbable(),
    'doors': Door(),
    'hazards': Hazards(),
    'door_start': (69, 1),
    'tile_list': tile_list,
    'gem_list': gem_list,
    'cur_level_mobs': [
        ([
            (2030, 160),
            (1880, 210),
            (1730, 170),
            (1630, 210),
            (1555, 180),
            (1605, 160)]
            , mobs,
            "spider"),
        ([
            (1250, 170),
            (1150, 210),
            (1075, 180),
            (1125, 160),
            (1550, 160),
            (1400, 210)]
            , mobs,
            "spider")]
    }


"""level 4"""

gem_list = [("trophy", (6, 1)), ("red_gem", (48, 1)), ("red_gem", (54, 5)),
                    ("jetpack", (69, 4)), ("wand", (79, 6)), ("ring", (90, 5)), ("crown", (97, 1))]
blue_gems = [(2, 6), (6, 6), (8, 5), (10, 4), (12, 1), (20, 1), (25, 1), (29, 1), (27, 4),
                (39, 4), (44, 3), (42, 1), (45, 1), (55, 1), (55, 3), (56, 5), (57, 6), (59, 1),
                (62, 1), (66, 2), (78, 1), (78, 3), (81, 4), (85, 5), (86, 6), (94, 1), (94, 7),
                (96, 1)]
for j in range(3):
    blue_gems.append((71, 3 + j))
for j in range(4):
    blue_gems.append((75, 1 + j))
for i in range(5):
    blue_gems.append((80 + 3 * i, 1))
for gem_location in blue_gems:
    gem_list.append(("blue_gem", gem_location))

tile_list = [("vertical_pipe", (1, 4))]
blue_bricks = [(1, 3), (2, 4), (2, 5), (7, 1), (11, 6), (18, 4), (19, 6), (20, 2), (21, 5),
                (23, 3), (24, 5), (25, 5), (38, 4), (44, 7), (45, 3), (47, 1), (47, 2),
                (50, 3), (51, 3), (53, 6), (53, 5), (57, 5), (59, 5), (59, 6), (62, 4),
                (62, 7), (62, 8), (64, 5), (64, 6), (65, 6), (67, 6), (68, 6), (68, 2),
                (69, 2), (69, 8), (70, 3), (70, 4), (72, 8), (80, 6), (80, 5), (81, 5),
                (82, 7), (85, 4), (86, 5), (92, 4), (95, 5), (95, 7), (97, 8)]
for i in range(100):
    blue_bricks.append((i, 0))
for i in range(28):
    blue_bricks.append((i, 9))
for i in range(6):
    blue_bricks.append((8 + i, 8))
for i in range(4):
    blue_bricks.append((9 + i, 7))
for i in range(5):
    blue_bricks.append((3 + i, 2))
for i in range(4):
    blue_bricks.append((13 + i, 3))
for i in range(5):
    blue_bricks.append((27 + i, 3))
for i in range(3):
    blue_bricks.append((30 + i, 6))
for i in range(64):
    blue_bricks.append((35 + i, 9))
for i in range(3):
    blue_bricks.append((35 + i, 2))
for i in range(7):
    blue_bricks.append((39 + i, 2))
for i in range(5):
    blue_bricks.append((38 + i, 5))
for i in range(5):
    blue_bricks.append((38 + i, 7))
for i in range(4):
    blue_bricks.append((48 + i, 5))
for i in range(7):
    blue_bricks.append((51 + i, 2))
for i in range(6):
    blue_bricks.append((49 + i, 7))
for i in range(5):
    blue_bricks.append((53 + i, 4))
for i in range(4):
    blue_bricks.append((56 + i, 7))
for i in range(3):
    blue_bricks.append((61 + i, 3))
for i in range(3):
    blue_bricks.append((65 + i, 3))
for i in range(3):
    blue_bricks.append((68 + i, 5))
for i in range(3):
    blue_bricks.append((75 + i, 6))
for i in range(4):
    blue_bricks.append((77 + i, 7))
for i in range(4):
    blue_bricks.append((77 + i, 4))
for i in range(13):
    blue_bricks.append((78 + i, 2))
for i in range(4):
    blue_bricks.append((87 + i, 6))
for i in range(4):
    blue_bricks.append((93 + i, 6))
for i in range(3):
    blue_bricks.append((95 + i, 3))
for j in range(10):
    blue_bricks.append((0, j))
for j in range(3):
    blue_bricks.append((16, 6 + j))
for j in range(5):
    blue_bricks.append((35, 4 + j))
for j in range(3):
    blue_bricks.append((47, 5 + j))
for j in range(5):
    blue_bricks.append((72, 2 + j))
for j in range(4):
    blue_bricks.append((76, 1 + j))
for j in range(4):
    blue_bricks.append((83, 4 + j))
for i in range(2):
    for j in range(8):
        blue_bricks.append((98 + i, 1 + j))
for i in range(3):
    for j in range(4):
        blue_bricks.append((3 + i + j * 2, 6 - j))
for j in range(3):
    for i in range(6 - 2 * j):
        blue_bricks.append((22 + j + i, 8 - j))
for brick_location in blue_bricks:
    tile_list.append(("blue_brick", brick_location))

hazard_list = [("fire", (3, 5)), ("fire", (4, 5)), ("water", (50, 2)), ("water", (54, 6)),
                ("water", (67, 2)), ("water", (70, 2)), ("purple_fire", (78, 6)),
                ("purple_fire", (93, 5)), ("purple_fire", (94, 5))]
for i in range(8):
    hazard_list.append(("fire", (28 + i, 9)))
for j in range(3):
    hazard_list.append(("water", (58, 4 + j)))
for i in range(3):
    hazard_list.append(("purple_fire", (87 + i, 5)))

level_items[4] = {
    'mobs': mobs,
    'hazard_list': hazard_list,
    'dave_pos': (32, 202),
    'tiles': Tiles(),
    'gems': Gems(),
    'climbable': Climbable(),
    'doors': Door(),
    'hazards': Hazards(),
    'door_start': (97, 2),
    'tile_list': tile_list,
    'gem_list': gem_list,
    'cur_level_mobs': [
        ([
            (940, 290),
            (1100, 290),
            (1075, 175),
            (1040, 100),
            (850, 120),
            (850, 180),
        ]
            , mobs,
            "spinner")

            ]
    }


""""level 5"""

gem_list = [("purple_gem", (3, 4)), ("purple_gem", (5, 4)), ("gun", (15, 6)),
                    ("purple_gem", (29, 4)), ("purple_gem", (33, 5)), ("jetpack", (37, 3)),
                    ("purple_gem", (42, 3)), ("purple_gem", (44, 3)), ("trophy", (47, 2)),
                    ("red_gem", (54, 2)), ("red_gem", (57, 2)), ("red_gem", (64, 8)),
                    ("blue_gem", (67, 1)), ("blue_gem", (67, 6)), ("blue_gem", (69, 5)),
                    ("blue_gem", (70, 1)), ("blue_gem", (73, 1)), ("blue_gem", (76, 6)),
                    ("purple_gem", (77, 1)), ("purple_gem", (79, 1)), ("purple_gem", (80, 5)),
                    ("purple_gem", (82, 5)), ("purple_gem", (83, 1)), ("purple_gem", (85, 1)),
                    ("red_gem", (91, 1)), ("red_gem", (94, 4)), ("crown", (96, 1))]

tile_list = [("dirt_ll", (0, 0)), ("horizontal_pipe", (1, 8)), ("dirt_ul", (60, 3)),
                ("dirt_ul", (61, 2)), ("dirt_ul", (63, 1)), ("vertical_pipe", (78, 1)),
                ("vertical_pipe", (84, 1)), ("dirt_ll", (99, 0)), ("dirt_ul", (99, 9))]
clay_locations = [(26, 5), (29, 5), (30, 7), (33, 6), (36, 6), (39, 5), (41, 6), (53, 7),
                    (54, 3), (55, 5), (57, 3), (57, 8), (60, 7), (63, 5), (69, 6), (85, 7),
                    (87, 2), (87, 6), (89, 4), (89, 7), (91, 2), (91, 6), (93, 7)]
dirt_locations = [(62, 1), (70, 8), (71, 8), (98, 2)]
for j in range(8):
    dirt_locations.append((0, 1 + j))
for i in range(25):
    dirt_locations.append((i, 9))
for i in range(5):
    dirt_locations.append((i + 9, 8))
for j in range(2):
    for i in range(3):
        dirt_locations.append((i + 10, 6 + j))
for i in range(13):
    dirt_locations.append((42 + i, 9))
for i in range(37):
    dirt_locations.append((i + 58, 0))
for i in range(34):
    dirt_locations.append((i + 65, 9))
for i in range(3):
    dirt_locations.append((i + 96, 0))
for i in range(3):
    dirt_locations.append((i + 97, 1))
for i in range(3):
    dirt_locations.append((i + 97, 8))
for j in range(6):
    dirt_locations.append((99, 2 + j))
for j in range(2):
    for i in range(5):
        dirt_locations.append((i + 20, 7 + j))
for j in range(2):
    for i in range(3):
        dirt_locations.append((i + 42, 7 + j))
for j in range(3):
    for i in range(4 - j):
        dirt_locations.append((i + 58, 1 + j))
for i in range(2):
    for j in range(5 + i):
        dirt_locations.append((65 + i, 8 - j))
for j in range(3):
    for i in range(4):
        dirt_locations.append((i + 72, 4 + j))
for location in dirt_locations:
    tile_list.append(("dirt", location))
for location in clay_locations:
    tile_list.append(("clay", location))

hazard_list = [("purple_fire", (71, 5)), ("purple_fire", (72, 8)), ("purple_fire", (74, 7)),
                ("purple_fire", (76, 8))]
for i in range(17):
    hazard_list.append(("water", (25 + i, 9)))
for i in range(10):
    hazard_list.append(("fire", (55 + i, 9)))
for i in range(3):
    hazard_list.append(("water", (67 + i, 8)))

decoration_list = []
grass_locations = [(2, 8), (3, 8), (9, 7), (13, 7), (42, 6), (44, 6), (65, 3), (66, 2), (70, 7),
                    (71, 7)]
for i in range(4):
    grass_locations.append((i + 5, 8))
for i in range(3):
    grass_locations.append((i + 10, 5))
for i in range(6):
    grass_locations.append((i + 14, 8))
for i in range(5):
    grass_locations.append((i + 20, 6))
for i in range(10):
    grass_locations.append((i + 45, 8))
for i in range(4):
    grass_locations.append((i + 72, 3))
for i in range(3):
    grass_locations.append((i + 73, 8))
for i in range(4):
    grass_locations.append((i + 77, 8))
for i in range(15):
    grass_locations.append((i + 82, 8))
for location in grass_locations:
    decoration_list.append(("grass", location))

climbable_list = [("leaves_ur", (2, 3)), ("leaves_ul", (6, 3)), ("leaves_br", (2, 1)),
                    ("leaves_br", (3, 0)), ("leaves_bl", (5, 0)), ("leaves_bl", (6, 1)),
                    ("moon", (30, 1)), ("leaves_ur", (41, 2)), ("leaves_ul", (45, 2)),
                    ("leaves_ur", (80, 4)), ("leaves_ul", (82, 4)), ("leaves_br", (80, 2)),
                    ("leaves_bl", (82, 2)), ]
leaf_list = [(81, 2), (81, 4)]
star_list = [(1, 4), (2, 0), (8, 0), (8, 2), (10, 1), (12, 0), (13, 2), (14, 1), (16, 2),
                (17, 1), (19, 0), (21, 2), (23, 0), (24, 1), (26, 0), (28, 1), (30, 0),
                (33, 0), (36, 0), (39, 1), (40, 0), (47, 0), (48, 1), (50, 1), (51, 0),
                (53, 0)]
for i in range(3):
    leaf_list.append((3 + i, 3))
for j in range(3):
    for i in range(1 + 2 * j):
        leaf_list.append((4 + i - j, j))
for i in range(3):
    leaf_list.append((42 + i, 2))
for i in range(3):
    leaf_list.append((80 + i, 3))
for j in range(2):
    for i in range(5):
        leaf_list.append((41 + i, j))
for location in leaf_list:
    climbable_list.append(("leaves", location))
for location in star_list:
    climbable_list.append(("stars", location))
for j in range(5):
    climbable_list.append(("tree_trunk", (4, 4 + j)))
for j in range(4):
    climbable_list.append(("tree_trunk", (43, 3 + j)))
for j in range(4):
    climbable_list.append(("tree_trunk", (81, 5 + j)))

level_items[5] = {
    'mobs': mobs,
    'hazard_list': hazard_list,
    'dave_pos': (64, 298),
    'tiles': Tiles(),
    'gems': Gems(),
    'climbable': Climbable(),
    'doors': Door(),
    'hazards': Hazards(),
    'door_start': (97, 3),
    'tile_list': tile_list,
    'gem_list': gem_list,
    'climbable_list': climbable_list,
    'cur_level_mobs': [
        ([
            (2030, 160),
            (1880, 210),
            (1730, 170),
            (1630, 210),
            (1555, 180),
            (1605, 160)]
            , mobs,
            "spider"),
        ([
            (1250, 170),
            (1150, 210),
            (1075, 180),
            (1125, 160),
            (1550, 160),
            (1400, 210)]
            , mobs,
            "spider")]
    }
