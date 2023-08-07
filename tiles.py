import pygame
from render import SpriteSheet


class Tiles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)

    def tile(self):
        return self.sprite_sheet.get_sprite(1, 7, 16, 16, 2)
