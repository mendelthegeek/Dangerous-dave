from banner import *
from player import *
from tiles import *

board = pygame.display.set_mode((640, 392))


def next_level(curr_score):
    tiles = Tiles()
    doors = Door()
    for i in range(20):
        tiles.create_tile("blue_brick", (i * 32, 138))
    board.blit(*doors.create_tile((0, 170)))
    for i in range(20):
        tiles.create_tile("blue_brick", (i * 32, 202))
    dave = Dave((32, 170))
    dave.x_speed = 1

    while dave.x < 608:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        board.fill(BG)

        for door in doors.sprites():
            board.blit(door.image, door.rect)
        for tile in tiles.sprites():
            board.blit(tile.image, tile.rect)
        current_time = pygame.time.get_ticks()
        if current_time - dave.last_update > dave.speed:
            dave.move()
            dave.last_update = current_time

        board.blit(dave.current_display(), dave.position())
        blit_border(board, curr_score)
        pygame.display.flip()
    return True


def init_tiles(tiles, gems, doors):
    gem_list = [
        ("blue_gem", (32, 234)),
        ("blue_gem", (224, 234)),
        ("blue_gem", (32, 170)),
        ("blue_gem", (160, 170)),
        ("blue_gem", (288, 170)),
        ("blue_gem", (416, 170)),
        ("blue_gem", (544, 170)),
        ("blue_gem", (96, 106)),
        ("blue_gem", (224, 106)),
        ("blue_gem", (480, 106)),
        ("red_gem", (544, 74)),
        ("purple_gem", (32, 74)),
    ]
    tiles.create_tile("horizontal_pipe", (32, 298))
    for i in range(4):
        tiles.create_tile("red_brick", (96 + i * 128, 138))
    for i in range(5):
        tiles.create_tile("red_brick", (32 + i * 128, 202))
    for i in range(4):
        tiles.create_tile("red_brick", (128 + i * 32, 266))
    for i in range(6):
        tiles.create_tile("red_brick", (352 + i * 32, 266))
    tiles.create_tile("red_brick", (352, 298))
    board.blit(*doors.create_tile((384, 298)))

    for j in range(10):
        tiles.create_tile("red_brick", (0, 42 + j * 32))
    for j in range(10):
        tiles.create_tile("red_brick", (608, 42 + j * 32))
    for j in range(10):
        tiles.create_tile("red_brick", (576, 42 + j * 32))
    for i in range(20):
        tiles.create_tile("red_brick", (i * 32, 42))
    for i in range(20):
        tiles.create_tile("red_brick", (i * 32, 330))

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
