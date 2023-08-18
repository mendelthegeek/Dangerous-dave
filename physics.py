import operator
from itertools import groupby

import pygame

arr = set()


def check_collision(dave, tiles):
    # check for side,top or bottom collisions.
    # offset by one since collisions happen only after sprites overlap

    # detects any collisions and puts them into an array
    detect_collision = pygame.sprite.spritecollide(dave, tiles, False)
    # a bit more convenient types to work with
    collided = [pygame.Rect(tile) for tile in set(tuple(tile.rect) for tile in detect_collision)]
    # this variable is to avoid treating horizontal collisions as vertical collisions.
    side_collide = False
    # check for side collisions
    for tile in collided:
        # check that (1) tile isn't below dave (2) tile isn't above dave
        if tile.top + 1 < dave.rect.bottom and not tile.bottom == dave.rect.top + 1:
            if dave.rect.right - 1 == tile.left:
                side_collide = True
                dave.x_speed = min(dave.x_speed, 0)
            elif dave.rect.left + 1 == tile.right:
                side_collide = True
                dave.x_speed = max(dave.x_speed, 0)

    # reset variable
    dave.on_surface = False

    dave_column = (dave.rect.left + 7) // 32
    for tile in collided:
        if dave_column == tile.left // 32:
            if dave.rect.bottom - 1 == tile.top:
                dave.on_surface = True
            elif dave.rect.top + 1 == tile.bottom:
                dave.jump_height = 0

    if dave.rect.bottom - 1 in [tile.top for tile in collided]:
        # check if we aren't confusing a side collision for a bottom collision
        if not side_collide:
            dave.on_surface = True
    # check if we bumped our head ouchie
    if dave.rect.top + 1 in [tile.bottom for tile in collided]:
        if not side_collide:
            dave.jump_height = 0


def check_obtained(dave, obtainables):
    points = 0
    detect_collision = pygame.sprite.spritecollide(dave, obtainables, True)
    for obtained in detect_collision:
        points += obtained.value
        if obtained.gem_type == "trophy":
            dave.has_key = True
        if obtained.gem_type == "gun":
            dave.has_gun = True
        if obtained.gem_type == "jetpack":
            dave.jetpack = 50
    return points


def check_door(dave, doors):
    return pygame.sprite.spritecollide(dave, doors, False) and dave.has_key


def check_death(dave, hazards):
    return pygame.sprite.spritecollide(dave, hazards, False)
