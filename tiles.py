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


class Gems(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)
        self.tileset = {
            "blue_gem": (5, 1),
            "red_gem": (5, 2)
        }
        self.point_values = {
            "blue_gem": 100,
            "red_gem": 200
        }

    def create_tile(self, gem_type, rect):
        sheet_location = self.tileset[gem_type]
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(*rect, 32, 32)
        sprite.value = self.point_values[gem_type]
        sprite.image = self.sprite_sheet.get_sprite(*sheet_location, 16, 16, 2)
        sprite.gem_type = gem_type
        self.add(sprite)
        return sprite.image, sprite.rect


class Trophy(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = pygame.Rect(*rect, 32, 32)
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)
        self.images = []
        for i in range(5):
            self.images.append(self.sprite_sheet.get_sprite(1, i, 16, 16, 2))
        self.frame = 0
        self.image = self.images[self.frame]
        self.last_updated = pygame.time.get_ticks()
        self.gem_type = "trophy"
        self.value = 1000

    def get_image(self):
        curr_time = pygame.time.get_ticks()
        if curr_time - self.last_updated > 150:
            self.frame = (self.frame + 1) % 5
            self.last_updated = curr_time
            self.image = self.images[self.frame]
        return self.image, self.rect

