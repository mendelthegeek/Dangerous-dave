from banner import *
from player import *
from tiles import *
from render import *
def next_level(curr_score):
    tiles = Tiles()
    doors = Door()
    for i in range(20):
        tiles.create_tile("blue_brick", (i * 32, 138))
    doors.create_tile((0, 170))
    for i in range(20):
        tiles.create_tile("blue_brick", (i * 32, 202))
    dave = Dave((32, 170))
    dave.x_speed = 1

    while dave.x < 608:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        render(dave, tiles, pygame.sprite.Group(), doors, curr_score)
    return True