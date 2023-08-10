import pygame
from player import *
from tiles import *
from render import *

pygame.init()

dave = Dave()
last_update = pygame.time.get_ticks()
run = True
tiles = Tiles()

icon = tiles.sprite_sheet.get_sprite(5, 4, 16, 16, 2)
pygame.display.set_caption("Dangerous Dave")
pygame.display.set_icon(icon)
while run:

    tiles = Tiles()
    last_update = test_render(dave, tiles, last_update)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dave.on_surface:
                    dave.jump_height += 64
            if event.key == pygame.K_RIGHT:
                dave.x_speed += 1
            if event.key == pygame.K_LEFT:
                dave.x_speed -= 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dave.x_speed -= 1
            if event.key == pygame.K_LEFT:
                dave.x_speed += 1

    detect_collision = pygame.sprite.spritecollide(dave, tiles, False)
    collided = [pygame.Rect(tile) for tile in set(tuple(tile.rect) for tile in detect_collision)]
    dave.on_surface = False
    if dave.rect.bottom-1 in [tile.top for tile in collided]:
        dave.on_surface = True
