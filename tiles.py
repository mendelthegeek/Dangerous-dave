import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite

from spritesheet import SpriteSheet


class Tile(pygame.sprite.Group):
    sprite_source: str
    sprite_sheet: SpriteSheet

    def __init__(self) -> None:
        super().__init__()
        self.sprite_source = r"resources/tileset/tileset.png"
        self.sprite_sheet = SpriteSheet(self)

    def render_tile(self, rect: tuple[int, int], sheet_locations: list[tuple[int, int]]) -> Sprite:
        sprite: Sprite = pygame.sprite.Sprite()
        sprite.rect = pygame.Rect(rect[0] * 32, rect[1] * 32 + 42, 32, 32)
        sprite.images: list[Surface] = []
        sheet_location: tuple[int, int]
        for sheet_location in sheet_locations:
            sprite.images.append(self.sprite_sheet.get_sprite(*sheet_location, 16, 16, 2))
        sprite.last_updated: int = pygame.time.get_ticks()
        sprite.frame: int = 0
        self.add(sprite)
        return sprite

    @staticmethod
    def get_image(sprite: Sprite) -> Surface:
        curr_time: int = pygame.time.get_ticks()
        if curr_time - sprite.last_updated > 150:
            sprite.frame = (sprite.frame + 1) % len(sprite.images)
            sprite.last_updated = curr_time
        return sprite.images[sprite.frame]


class Tiles(Tile):
    tileset: dict[str, list[tuple[int, int]]]

    def __init__(self) -> None:
        super().__init__()
        self.tileset = {
            "red_brick": [(1, 7)],
            "blue_brick": [(0, 4)],
            "horizontal_pipe": [(1, 5)],
            "vertical_pipe": [(1, 6)],
            "purple_horizontal": [(3, 2)],
            "clay": [(0, 0)],
            "blue_pillar": [(2, 0)],
            "dirt": [(1, 8)],
            "dirt_ll": [(2, 2)],
            "dirt_ul": [(2, 3)],
            "dirt_ur": [(2, 4)],
            "dirt_lr": [(2, 5)]
        }

    def create_tile(self, tile_type: str, rect: tuple[int, int]) -> None:
        sheet_locations: list[tuple[int, int]] = self.tileset[tile_type]
        self.render_tile(rect, sheet_locations)

    def render_image(self, sprite: Sprite) -> tuple[Surface, tuple[int, int]]:
        return self.get_image(sprite), sprite.rect


class Gems(Tile):
    point_values: dict[str, int]
    tileset: dict[str, list[tuple[int, int]]]

    def __init__(self) -> None:
        super().__init__()
        self.tileset = {
            "blue_gem": [(5, 1)],
            "purple_gem": [(5, 2)],
            "red_gem": [(5, 3)],
            "crown": [(5, 4)],
            "ring": [(5, 5)],
            "wand": [(5, 6)],
            "trophy": [(1, i) for i in range(5)],
            "gun": [(2, 1)],
            "jetpack": [(0, 3)]
        }
        self.point_values = {
            "purple_gem": 50,
            "blue_gem": 100,
            "red_gem": 150,
            "ring": 200,
            "crown": 300,
            "wand": 500,
            "trophy": 1000,
            "gun": 0,
            "jetpack": 0
        }

    def create_tile(self, gem_type: str, rect: tuple[int, int]) -> None:
        sheet_locations: list[tuple[int, int]] = self.tileset[gem_type]
        sprite: Sprite = self.render_tile(rect, sheet_locations)
        sprite.rect: Rect = self.pad(sprite.rect)
        sprite.value: int = self.point_values[gem_type]
        sprite.gem_type: str = gem_type

    @staticmethod
    def pad(rect: Rect) -> Rect:
        return pygame.Rect(rect.left - 5, rect.top, rect.width + 10, rect.height)

    @staticmethod
    def unpad(rect: Rect) -> Rect:
        return pygame.Rect(rect.left + 5, rect.top, rect.width - 10, rect.height)

    def render_image(self, sprite: Sprite) -> tuple[Surface, Rect]:
        return self.get_image(sprite), self.unpad(sprite.rect)


class Door(Tile):

    def __init__(self) -> None:
        super().__init__()

    def create_tile(self, rect: tuple[int, int]) -> None:
        sheet_locations: list[tuple[int, int]] = [(0, 1)]
        self.render_tile(rect, sheet_locations)

    def render_image(self, sprite: Sprite) -> tuple[Surface, Rect]:
        return self.get_image(sprite), sprite.rect


class Hazards(Tile):
    tileset: dict[str, list[tuple[int, int]]]

    def __init__(self) -> None:
        super().__init__()
        self.tileset = {
            "fire": [(0, i + 5) for i in range(4)],
            "water": [(4, i) for i in range(4)] + [(3, 8)],
            "purple_fire": [(2, i + 6) for i in range(3)] + [(3, 0)]
        }

    def create_tile(self, tile_type: str, rect: tuple[int, int]) -> Sprite:
        sheet_locations: list[tuple[int, int]] = self.tileset[tile_type]
        sprite: Sprite = self.render_tile(rect, sheet_locations)
        return sprite

    def render_image(self, sprite: Sprite) -> tuple[Surface, Rect]:
        return self.get_image(sprite), sprite.rect


class Passable(Tile):

    tileset: dict[str, list[tuple[int, int]]]

    def __init__(self) -> None:
        super().__init__()
        self.tileset = {
            "purple_pipe": [(3, 3)],
            "grass": [(3, 4)],
        }

    def create_tile(self, tile_type: str, rect: tuple[int, int]) -> None:
        sheet_locations: list[tuple[int, int]] = self.tileset[tile_type]
        self.render_tile(rect, sheet_locations)

    def render_image(self, sprite: Sprite) -> tuple[Surface, Rect]:
        return self.get_image(sprite), sprite.rect


class Climbable(Tile):
    tileset: dict[str, list[tuple[int, int]]]

    def __init__(self) -> None:
        super().__init__()
        self.tileset = {
            "tree_trunk": [(3, 5)],
            "leaves": [(3, 6)],
            "leaves_br": [(4, 6)],
            "leaves_bl": [(4, 7)],
            "leaves_ur": [(4, 8)],
            "leaves_ul": [(5, 0)],
            "stars": [(4, 4)],
            "moon": [(4, 5)]
        }

    def create_tile(self, tile_type: str, rect: tuple[int, int]) -> None:
        sheet_locations: list[tuple[int, int]] = self.tileset[tile_type]
        self.render_tile(rect, sheet_locations)

    def render_image(self, sprite: Sprite) -> tuple[Surface, Rect]:
        return self.get_image(sprite), sprite.rect
