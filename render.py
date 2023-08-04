from player import *

BG = (50, 50, 50)

board = pygame.display.set_mode((500, 500))


def test_render(dave):
    board.fill(BG)

    sprite_sheet = SpriteSheet(dave.sprite_source)

    board.blit(sprite_sheet.get_dave_sprite(0, 24, 16, 2), dave.position)
    board.blit(sprite_sheet.get_dave_sprite(3, 24, 16, 10), (250, 0))
    pygame.display.flip()


class SpriteSheet:

    def __init__(self, source):
        self.sprite_sheet = pygame.image.load(source)

    def get_dave_sprite(self, frame, width, height, scale):
        dave_sprite = pygame.Surface((width, height)).convert_alpha()
        sprite_rectangle = ((frame * (width + 1)) + 1, 1, (1 + width * (frame + 1)), height + 1)
        dave_sprite.blit(self.sprite_sheet, (0, 0), sprite_rectangle)
        dave_sprite = pygame.transform.scale(dave_sprite, (width * scale, height * scale))
        dave_sprite.set_colorkey((0, 0, 0))
        return dave_sprite
