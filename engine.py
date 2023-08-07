import pygame
from player import *
from tiles import *
from render import *

pygame.init()

dave = Dave()
last_update = pygame.time.get_ticks()


tiles = Tiles()

run = True
while run:
    last_update = test_render(dave, tiles, last_update)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dave.velocity == 0:
                    dave.velocity += 96
            if event.key == pygame.K_RIGHT:
                dave.moving_right = True
            if event.key == pygame.K_LEFT:
                dave.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dave.moving_right = False
            if event.key == pygame.K_LEFT:
                dave.moving_left = False
