import pygame
from render import SpriteSheet


class Tiles(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)
        self.tileset = {
            "red_brick": (1, 7),
            "horizontal_pipe": (1, 5)
        }

    def create_tile(self, tile_type, rect):
        sheet_location = self.tileset[tile_type]
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(*rect, 32, 32)
        sprite.image = self.sprite_sheet.get_sprite(*sheet_location, 16, 16, 2)
        self.add(sprite)
        return sprite.image, sprite.rect
        self.add(sprite)
        image = self.sprite_sheet.get_sprite(*sheet_location, 16, 16, 2)
        return image, sprite.rect