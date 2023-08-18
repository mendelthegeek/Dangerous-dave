import pygame
from spritesheet import SpriteSheet


class Tile(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)

    def render_tile(self, rect, sheet_locations):
        sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(rect[0] * 32, rect[1] * 32 + 42, 32, 32)
        sprite.images = []
        for sheet_location in sheet_locations:
            sprite.images.append(self.sprite_sheet.get_sprite(*sheet_location, 16, 16, 2))
        sprite.last_updated = pygame.time.get_ticks()
        sprite.frame = 0
        self.add(sprite)
        return sprite

    def get_image(self, sprite):
        curr_time = pygame.time.get_ticks()
        if curr_time - sprite.last_updated > 150:
            sprite.frame = (sprite.frame + 1) % len(sprite.images)
            sprite.last_updated = curr_time
        return sprite.images[sprite.frame]


class Tiles(Tile):
    def __init__(self):
        super().__init__()
        self.tileset = {
            "red_brick": [(1, 7)],
            "blue_brick": [(0, 4)],
            "horizontal_pipe": [(1, 5)],
            "purple_horizontal": [(3, 2)],
            "clay": [(0, 0)],
            "dirt": [(1, 8)],
            "dirt_ll": [(2, 2)],
            "dirt_ul": [(2, 3)],
            "dirt_ur": [(2, 4)],
            "dirt_lr": [(2, 5)]
        }

    def create_tile(self, tile_type, rect):
        sheet_locations = self.tileset[tile_type]
        sprite = self.render_tile(rect, sheet_locations)

    def render_image(self, sprite):
        return self.get_image(sprite), sprite.rect


class Gems(Tile):
    def __init__(self):
        super().__init__()
        self.tileset = {
            "blue_gem": [(5, 1)],
            "purple_gem": [(5, 2)],
            "red_gem": [(5, 3)],
            "crown": [(5, 4)],
            "ring": [(5, 5)],
            "wand": [(5, 6)],
            "trophy": [(1, i) for i in range(5)]
        }
        self.point_values = {
            "purple_gem": 50,
            "blue_gem": 100,
            "red_gem": 150,
            "ring": 200,
            "crown": 300,
            "wand": 500,
            "trophy": 1000
        }

    def create_tile(self, gem_type, rect):
        sheet_locations = self.tileset[gem_type]
        sprite = self.render_tile(rect, sheet_locations)
        sprite.rect = self.pad(sprite.rect)
        sprite.value = self.point_values[gem_type]
        sprite.gem_type = gem_type

    def pad(self, rect):
        return pygame.Rect(rect.left - 5, rect.top, rect.width + 10, rect.height)

    def unpad(self, rect):
        return pygame.Rect(rect.left + 5, rect.top, rect.width - 10, rect.height)

    def render_image(self, sprite):
        return self.get_image(sprite), self.unpad(sprite.rect)


class Door(Tile):

    def __init__(self):
        super().__init__()

    def create_tile(self, rect):
        sheet_locations = [(0, 1)]
        self.render_tile(rect, sheet_locations)

    def render_image(self, sprite):
        return self.get_image(sprite), sprite.rect


class Hazards(Tile):
    def __init__(self):
        super().__init__()
        self.tileset = {
            "fire": [(0, i + 5) for i in range(4)],
            "water": [(4, i) for i in range(4)] + [(3,8)],
            "purple_fire": [(2, i+6) for i in range(3)] + [(3, 0)]
        }

    def create_tile(self, tile_type, rect):
        sheet_locations = self.tileset[tile_type]
        sprite = self.render_tile(rect, sheet_locations)
        return sprite

    def render_image(self, sprite):
        return self.get_image(sprite), sprite.rect
