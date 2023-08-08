import pygame
from render import SpriteSheet


class Tiles(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)

    def red_brick(self):
        return self.sprite_sheet.get_sprite(1, 7, 16, 16, 2)

    def horizontal_pipe(self):
        return self.sprite_sheet.get_sprite(1, 5, 16, 16, 2)
