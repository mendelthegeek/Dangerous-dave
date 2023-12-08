import pygame
from pygame import Surface
from pygame.sprite import Sprite

from tiles import Tile


class SpriteSheet:

    frame: int
    sprite_sheet: Surface

    def __init__(self, sprite: Sprite | Tile) -> None:
        self.sprite = sprite
        self.sprite_sheet = pygame.image.load(self.sprite.sprite_source)
        self.frame = 0

    def get_sprite(self, row: int, column: int, width: int, height: int, scale: int) -> Surface:
        sprite: Surface = pygame.Surface((width, height)).convert_alpha()
        sprite_rectangle: tuple[int, int, int, int] = (
            (column * (width + 1)) + 1,
            1 + row * (height + 1),
            width,
            height
        )
        sprite.blit(self.sprite_sheet, (0, 0), sprite_rectangle)
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite.set_colorkey((0, 0, 0))
        return sprite

    def move_sprite(self, x: int, y: int) -> None:
        self.sprite.x += x
        self.sprite.y += y

    def move_frame(self) -> None:
        self.frame += 1
