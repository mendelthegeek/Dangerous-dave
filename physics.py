import operator
from itertools import groupby

import pygame


def check_collision(dave, tiles):
    side_collide = False
    detect_collision = pygame.sprite.spritecollide(dave, tiles, False)
    collided = [pygame.Rect(tile) for tile in set(tuple(tile.rect) for tile in detect_collision)]
    for tile in collided:
        if tile.top + 1 < dave.rect.bottom and not tile.bottom == dave.rect.top + 1:
            if dave.rect.right - 1 == tile.left:
                side_collide = True
                dave.x_speed = min(dave.x_speed, 0)
            elif dave.rect.left + 1 == tile.right:
                side_collide = True
                dave.x_speed = max(dave.x_speed, 0)
    dave.on_surface = False
    if dave.rect.bottom - 1 in [tile.top for tile in collided]:
        if not side_collide:
            dave.on_surface = True
        else:
            sorted_collisions = sorted(collided, key=operator.itemgetter(1))
            for k, g in groupby(sorted_collisions, operator.itemgetter(1)):
                if dave.rect.bottom - 1 == k and len(list(g)) > 1:
                    dave.on_surface = True
    if dave.rect.top + 1 in [tile.bottom for tile in collided] and not side_collide:
        dave.jump_height = 0
