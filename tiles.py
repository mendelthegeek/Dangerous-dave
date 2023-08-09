import pygame
from render import SpriteSheet


class Tiles(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)

    def red_brick(self, rect):
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(*rect, 16, 16)
        self.add(sprite)
        image = self.sprite_sheet.get_sprite(1, 7, 16, 16, 2)
        return image, sprite.rect

    def horizontal_pipe(self, rect):
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(*rect, 16, 16)
        self.add(sprite)
        image = self.sprite_sheet.get_sprite(1, 5, 16, 16, 2)
        return image, sprite.rect
