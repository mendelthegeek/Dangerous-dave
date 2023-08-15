from physics import *
from render import *
from levels import *


def start(curr_score=0):
    pygame.init()

    dave = Dave((64, 298))
    tiles = Tiles()
    icon = tiles.sprite_sheet.get_sprite(5, 4, 16, 16, 2)
    pygame.display.set_caption("Dangerous Dave")
    pygame.display.set_icon(icon)
    gems = Gems()
    doors = Door()
    hazards = Hazards()
    level_1(tiles, gems, doors)
    next_lev = False

    next_lev, curr_score = run(dave, tiles, hazards, gems, doors, curr_score)

    if next_lev:
        if next_level(curr_score):
            dave = Dave((64, 298))
            tiles = Tiles()
            doors = Door()
            gems = Gems()
            hazards = Hazards()
            level_2(tiles, hazards, gems, doors)

    next_lev, curr_score = run(dave, tiles, hazards, gems, doors, curr_score)


def run(dave, tiles, hazards, gems, doors, curr_score):
    running = True
    while running:
        if curr_score >= 100000:
            curr_score = 99999

        render(dave, tiles, hazards, gems, doors, curr_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, curr_score
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
        if check_death(dave, hazards):
            return False, curr_score
        if check_door(dave, doors):
            curr_score += 2000
            return True, curr_score


start()
