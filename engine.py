import pygame
from player import *
from render import *

pygame.init()

dave = Dave()
dave.__int__()
last_update = pygame.time.get_ticks()

run = True
while run:
    last_update = test_render(dave, last_update)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
