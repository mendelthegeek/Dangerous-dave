from __future__ import annotations

import os
import pygame
from pygame import Surface, SurfaceType, Vector2, Rect

from bullet import Bullet


class Mobs(pygame.sprite.Group):

    death_images: list[Surface | SurfaceType]

    def __init__(self) -> None:
        super().__init__()
        path: str = r"resources/dave/death"
        images: list[str] = os.listdir(path)
        self.death_images = [pygame.image.load(path + "//" + image) for image in images]

    def render_image(self, sprite: 'Mob') -> tuple[Surface, Rect]:
        sprite.pos: Vector2 = pygame.math.Vector2(sprite.rect.center)
        current_time: int = pygame.time.get_ticks()
        if sprite.dying:
            if current_time - sprite.last_update > 200:
                sprite.death_frame += 1
                sprite.last_update: int = current_time
                if sprite.death_frame == 7:
                    self.remove(sprite)
            return self.death_surface(self.death_images[sprite.death_frame]), sprite.rect
        if current_time - sprite.last_update > sprite.speed:
            sprite.update()
            sprite.last_update = current_time
            sprite.image_index += 1
            sprite.set_frame()
        return sprite.image, sprite.rect

    def death_surface(self, death_image: Surface) -> Surface:
        surface: Surface = pygame.Surface((49, 41)).convert_alpha()
        rectangle: tuple[int, int, int, int] = (0, 0, 49, 41)
        surface.blit(death_image, (0, 0), rectangle)
        surface = pygame.transform.scale(surface, (35, 30))
        surface.set_colorkey((0, 0, 0))
        return surface


class Mob(pygame.sprite.Sprite):

    image: Surface | SurfaceType
    bullet: Bullet | None
    death_frame: int
    dying: bool
    value: int
    image_index: int
    speed: int
    last_update: int
    target_radius: int
    target: tuple[int, int]
    waypoint_index: int
    waypoints: list[tuple[int, int]]
    rect: Rect
    pos: Vector2
    max_speed: float
    vel: Vector2
    y: int
    x: int
    mob_type: str

    def __init__(self, waypoints: list[tuple[int, int]], group: Mobs, mob_type: str, speed: int = 5) -> None:
        super().__init__()
        self.mob_type = mob_type
        self.x = waypoints[-1][0]
        self.y = waypoints[-1][1]
        self.vel = pygame.math.Vector2(0, 0)
        self.max_speed = 1.75
        self.pos = pygame.math.Vector2((self.x, self.y))
        self.rect = pygame.Rect((*self.pos, 54, 30))
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 50
        group.add(self)
        self.last_update = pygame.time.get_ticks()
        self.speed = speed
        self.value = 100
        self.image_index = 1
        self.set_frame()

        self.dying = False
        self.death_frame = -1

        self.bullet = None

    def update(self):
        self.target = self.waypoints[self.waypoint_index]
        # A vector pointing from self to the target.
        heading: Vector2 = self.target - self.pos
        distance: float = heading.length()  # Distance to the target.
        heading.normalize_ip()
        if distance <= 2:  # We're closer than 2 pixels.
            # Increment the waypoint index to switch the target.
            # The modulo sets the index back to 0 if it's equal to the length.
            self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
            self.target = self.waypoints[self.waypoint_index]
        if distance <= self.target_radius:
            # If we're approaching the target, we slow down.
            self.vel = heading * (distance / self.target_radius) ** .25 * self.max_speed
        else:  # Otherwise move with max_speed.
            self.vel = heading * self.max_speed

        self.pos += self.vel
        self.rect.center = self.pos

    def set_frame(self):
        mob_dir: list[str] = os.listdir(r"resources/mobs")
        animation_length: int = len([img for img in mob_dir if img.__contains__(self.mob_type)])
        self.image = pygame.image.load(
            r"resources/mobs/"
            f"{self.mob_type}{(self.image_index // 25) % animation_length}"
            r".png")
        self.image = pygame.transform.scale(
            self.image,
            (self.image.get_width() * 2 // 3, self.image.get_height() * 2 // 3))
        self.image.set_colorkey((0, 0, 0))

    def die(self):
        self.dying = True
