from physics import *
from player import *
from tiles import *
from render import *


def level(curr_score=0):
    pygame.init()

    dave = Dave((64, 298))
    run = True
    tiles = Tiles()
    icon = tiles.sprite_sheet.get_sprite(5, 4, 16, 16, 2)
    pygame.display.set_caption("Dangerous Dave")
    pygame.display.set_icon(icon)
    gems = Gems()
    doors = Door()
    init_tiles(tiles, gems, doors)
    next_lev = False
    while run:

        render(dave, tiles, gems, doors, curr_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        dave.x_speed = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if dave.on_surface and dave.jump_height == 0:
                dave.jump_height += 94
        if pressed[pygame.K_RIGHT]:
            dave.x_speed += 1
        if pressed[pygame.K_LEFT]:
            dave.x_speed -= 1

        curr_score += check_obtained(dave, gems)
        check_collision(dave, tiles)
        if check_door(dave, doors):
            run = False
            next_lev = True
            curr_score += 2000
        if curr_score >= 100000:
            curr_score = 99999
    if next_lev:
        if next_level(curr_score):
            level(curr_score)


level()
