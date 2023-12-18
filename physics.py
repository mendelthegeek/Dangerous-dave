from __future__ import annotations

from typing import List, Any

import pygame
from pygame import Rect
from pygame.rect import RectType
from pygame.sprite import Sprite

from bullet import Bullet
from monster import Mobs, Mob
from tiles import Tile, Gems, Door, Tiles

def collision_side_detect(dave: "Dave", game: "Game"):
    # detects any collisions and puts them into an array
    detect_collision: list[Tiles] = pygame.sprite.spritecollide(dave, game.level.tiles, False)
    # a bit more convenient types to work with
    collided: list[Rect] = [pygame.Rect(tile) for tile in set(tuple(tile.rect) for tile in detect_collision)]
    print("collisions", collided)
    side_detection(dave, collided)

def side_detection(dave: "Dave", collided: List[Rect]) -> bool:
    side_collide: bool = False
    # check for side collisions
    tile: Rect
    print(collided)
    for tile in collided:
        print(tile)
        # check that (1) tile isn't below dave (2) tile isn't above dave
        if tile.top + 1 < dave.rect.bottom and not tile.bottom == dave.rect.top + 1:
            print("parallel")
            print(dave.rect.left)
            if dave.rect.right - 1 == tile.left or dave.rect.right - 2 == tile.left:
                side_collide = True
                dave.x_speed = min(dave.x_speed, 0)
            elif dave.rect.left + 1 == tile.right or dave.rect.left + 2 == tile.right:
                print("proper detection")
                side_collide = True
                dave.x_speed = max(dave.x_speed, 0)
    return side_collide

def check_collision(dave: "Dave", tiles: Tile) -> None:
    # check for side,top or bottom collisions.
    # offset by one since collisions happen only after sprites overlap

    # detects any collisions and puts them into an array
    detect_collision: list[Tiles] = pygame.sprite.spritecollide(dave, tiles, False)
    # a bit more convenient types to work with
    collided: list[Rect] = [pygame.Rect(tile) for tile in set(tuple(tile.rect) for tile in detect_collision)]
    # this variable is to avoid treating horizontal collisions as vertical collisions.
    side_collide = side_detection(dave, collided)

    # reset variable
    dave.on_surface = False

    dave_column: int = (dave.rect.left + 7) // 32
    for tile in collided:
        if dave_column == tile.left // 32:
            if dave.rect.bottom - 1 == tile.top:
                dave.on_surface = True
            elif dave.rect.top + 1 == tile.bottom:
                dave.jump_height = 0

    if dave.rect.bottom - 1 in [tile.top for tile in collided] and not side_collide:
    # check if we aren't confusing a side collision for a bottom collision
        dave.on_surface = True
    # check if we bumped our head ouchie
    if dave.rect.top + 1 in [tile.bottom for tile in collided] and not side_collide:
        dave.jump_height = 0


def check_obtained(dave: "Dave", obtainables: Gems) -> int:
    points: int = 0
    detect_collision: list[Gems] = pygame.sprite.spritecollide(dave, obtainables, True)
    for obtained in detect_collision:
        points += obtained.value
        if obtained.gem_type == "trophy":
            dave.has_key = True
        if obtained.gem_type == "gun":
            dave.has_gun = True
        if obtained.gem_type == "jetpack":
            dave.jetpack = 120
    return points


def check_door(dave: "Dave", doors: Door) -> bool:
    return pygame.sprite.spritecollide(dave, doors, False) and dave.has_key


def check_death(game: "Game") -> bool:
    mobs: Mobs = game.level.mobs
    bullets: list[Bullet] = [mob.bullet for mob in mobs if mob.bullet is not None]
    return (bool(pygame.sprite.spritecollide(game.dave, game.level.hazards, False)) or
            any(pygame.sprite.collide_rect(game.dave, bullet) for bullet in bullets)
            or any(pygame.sprite.collide_rect(game.dave, mob) for mob in mobs))


def bullet_collision(game: "Game", bullet: Bullet, parent: "Dave" | Mob) -> None:
    if (bullet.x >= 640 or bullet.x <= 0 or
            pygame.sprite.spritecollide(bullet, game.level.tiles, False)):
        parent.bullet = None


def bullet_hit(game: "Game") -> None:
    collided: list[Mob] = pygame.sprite.spritecollide(game.dave.bullet, game.level.mobs, False)
    for mob in collided:
        if mob.dying:
            continue
        mob.die()
        game.score += mob.value
        game.dave.bullet = None


def check_climbing(game: "Game") -> bool:
    return bool(pygame.sprite.spritecollide(game.dave, game.level.climbable, False))


def check_climb_bottom(game: "Game") -> bool:
    detect_collision: list[Tiles] = pygame.sprite.spritecollide(game.dave, game.level.tiles, False)
    # a bit more convenient types to work with
    collided: list[Rect] = [pygame.Rect(tile) for tile in set(tuple(tile.rect) for tile in detect_collision)]
    dave_column: int = (game.dave.rect.left + 7) // 32
    for tile in collided:
        if dave_column == tile.left // 32:
            if game.dave.rect.bottom - 1 == tile.top:
                return True
    return False
