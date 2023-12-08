import pygame
from pygame import Surface
from pygame.sprite import Sprite

from tiles import Tile

#tried to fix error(pygame.error: No video mode has been set) by implementing a quick fix
pygame.init()
pygame.display.set_mode((1000, 800))

#at this point the game runs but its empty so i go back and actually call the make_level_map class metod

# then it gives me self.hazards.create_tile(self.level_items['Hazards'])
#TypeError: Hazards.create_tile() missing 1 required positional argument: 'rect

#then it gives me: self.hazards.create_tile(self.level_items['Hazards'])
#TypeError: Hazards.create_tile() missing 1 required positional argument: 'rect'

#in the end i coment out a few such things to just get it spinning and were back to the same problem of the screen basicly being empty to wich i check again that everything is properly added wich they seem to be (lelel_one_items dictionary that gets passed into class)

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
