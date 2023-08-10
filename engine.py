from physics import check_collision
from player import *
from tiles import *
from render import *

pygame.init()

dave = Dave()
last_update = pygame.time.get_ticks()
run = True
tiles = Tiles()
i = 1
icon = tiles.sprite_sheet.get_sprite(5, 4, 16, 16, 2)
pygame.display.set_caption("Dangerous Dave")
pygame.display.set_icon(icon)
while run:

    tiles = Tiles()
    last_update = test_render(dave, tiles, last_update)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    dave.x_speed = 0
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if dave.on_surface and dave.jump_height == 0:
            dave.jump_height += 64
    if pressed[pygame.K_RIGHT]:
        dave.x_speed += 1
    if pressed[pygame.K_LEFT]:
        dave.x_speed -= 1

    check_collision(dave, tiles)
