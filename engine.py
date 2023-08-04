import pygame
from player import *
from render import *

pygame.init()

run = True
while run:

    dave = Dave()
    dave.__int__()

    test_render(dave)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
