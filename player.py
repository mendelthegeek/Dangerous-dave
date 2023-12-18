from __future__ import annotations
import os

import pygame
from pygame import Surface, SurfaceType
from pygame.key import ScancodeWrapper

from bullet import Bullet
from physics import side_detection, collision_side_detect
from spritesheet import SpriteSheet

BG = (50, 50, 50)


class Dave(pygame.sprite.Sprite):
    last_update: int
    death_frame: int
    dying: bool
    death_images: list[Surface | SurfaceType]
    can_descend: bool
    climbing: bool
    dead: bool
    flying: bool
    bullet: Bullet | None
    has_gun: bool
    jetpack_last_update: int
    jetpack: int
    has_key: bool
    displayed: bool
    moved: bool
    facing: int
    y_speed: int
    jump_height: int
    sprite_sheet: SpriteSheet
    speed: int
    sprite_source: str
    y: int
    x: int
    on_surface: bool
    x_speed: int
    last_blinked: int

    def __init__(self, init_pos: tuple[int, int]) -> None:
        super().__init__()
        self.x, self.y = init_pos
        self.sprite_source = r"resources/dave/dave.png"

        self.speed = 8

        self.sprite_sheet = SpriteSheet(self)
        self.jump_height = 0

        self.x_speed = 0
        self.y_speed = 0
        self.facing = 0
        self.moved = False
        self.displayed = True
        self.on_surface = True
        self.last_blinked = pygame.time.get_ticks()
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.last_update = pygame.time.get_ticks()
        self.has_key = False
        self.jetpack = 0
        self.jetpack_last_update = pygame.time.get_ticks()
        self.has_gun = False
        self.bullet = None
        self.flying = False
        self.dead = False
        self.climbing = False
        self.can_descend = False

        path: str = r"resources/dave/death"
        images: list[str] = os.listdir(path)
        self.death_images = [pygame.image.load(path + "//" + image) for image in images]
        self.dying = False
        self.death_frame = -1

    def current_display(self) -> Surface:
        if self.speed == 2000:
            current_time: int = pygame.time.get_ticks()
            if current_time - self.last_update > 200:
                self.death_frame += 1
                self.last_update = current_time
            if self.death_frame == 7:
                self.dead = True
            return self.death_surface(self.death_images[self.death_frame])
        if not self.x_speed == 0:
            # expression maps 1 to 0 and -1 to 1, mapping movement to desired sprite sheet row
            self.facing = (1 - self.x_speed) // 2
        if self.flying:
            return self.sprite_sheet.get_sprite(
                self.facing, self.sprite_sheet.frame % 3 + 10, 24, 16, 2)
        if self.climbing:
            return self.sprite_sheet.get_sprite(
                self.facing, (self.sprite_sheet.frame // 5) % 3 + 7, 24, 16, 2)
        if not self.moved:
            current_ticks = pygame.time.get_ticks()
            if current_ticks - self.last_blinked > 500:
                self.last_blinked = current_ticks
                self.displayed = not self.displayed
            if self.displayed:
                empty_square: Surface = (pygame.Surface((24, 16)))
                empty_square.fill(BG)
                return empty_square
            elif not self.displayed:
                return self.sprite_sheet.get_sprite(0, 6, 24, 16, 2)
        if self.on_surface:
            return self.sprite_sheet.get_sprite(
                self.facing, self.sprite_sheet.frame // 8 % 4, 24, 16, 2)
        else:
            return self.sprite_sheet.get_sprite(self.facing, 5, 24, 16, 2)


    def position(self) -> tuple[int, int]:
        return self.x, self.y

    def move(self, game: "Game") -> None:
        print("start pos", self.x)
        print("dave speed start", self.x_speed)
        current_time: int = pygame.time.get_ticks()
        if current_time - self.last_update <= self.speed:
            return
        self.last_update = current_time
        if not self.x_speed == 0 or self.flying:
            self.sprite_sheet.move_frame()
            self.decrease_jetpack()
        self.jump()
        if self.climbing:
            self.climb()
            collision_side_detect(self, game)
        print("mid pos", self.x)
        print("dave speed mid", self.x_speed)
        self.x += self.x_speed * 1.2
        print("end pos", self.x)
        self.y = (self.y + self.y_speed) % 424
        self.move_rect()

    def climb(self) -> None:
        self.x_speed = 0
        self.y_speed = 0
        pressed: ScancodeWrapper = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.x_speed += 1
        if pressed[pygame.K_LEFT]:
            self.x_speed -= 1
        if pressed[pygame.K_UP]:
            self.y_speed -= 1
        if pressed[pygame.K_DOWN] and self.can_descend:
            self.y_speed += 1
        if abs(self.y_speed) > 0:
            self.sprite_sheet.move_frame()

    def jump(self) -> None:
        if self.jump_height == 0 and self.moved:
            if not self.on_surface:
                self.y_speed = 1
            else:
                self.y_speed = 0
        if self.jump_height > 0:
            self.jump_height -= 1
            if self.jump_height > 29:
                self.y_speed = -1
            else:
                self.y_speed = 0

    def move_rect(self) -> None:
        self.rect.update(self.x + 8, self.y, 14, 32)

    def die(self) -> None:
        self.speed = 2000

    def death_surface(self, death_image: Surface) -> Surface:
        surface: Surface = pygame.Surface((49, 41)).convert_alpha()
        rectangle: tuple[int, int, int, int] = (0, 0, 49, 41)
        surface.blit(death_image, (0, 0), rectangle)
        surface = pygame.transform.scale(surface, (35, 30))
        surface.set_colorkey((0, 0, 0))
        return surface

    def decrease_jetpack(self) -> None:
        curr_ticks: int = pygame.time.get_ticks()
        if curr_ticks - self.jetpack_last_update > 100:
            if self.flying:
                self.jetpack -= 1
                if self.jetpack == 0:
                    self.flying = False
            self.jetpack_last_update = curr_ticks

    def obtained(self) -> tuple[int, bool, bool]:
        return self.jetpack, self.has_gun, self.has_key

    def reset_obtained(self, obtained: tuple[int, bool, bool]) -> None:
        self.jetpack = obtained[0]
        self.has_gun = obtained[1]
        self.has_key = obtained[2]
