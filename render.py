from player import *

BG = (50, 50, 50)

board = pygame.display.set_mode((500, 500))


def test_render(dave):
    board.fill(BG)

    board.blit(get_dave_sprite(dave.sprite_images, 0, 24, 16, 2), dave.position)
    board.blit(get_dave_sprite(dave.sprite_images, 3, 24, 16, 5), (250, 0))
    pygame.display.flip()


def get_dave_sprite(sprite_sheet, sheet, width, height, scale):
    dave_sprite = pygame.Surface((width, height)).convert_alpha()
    dave_sprite.blit(sprite_sheet, (0, 0), ((sheet * (width + 1)) + 1, 1, (1 + width * (sheet + 1)), height + 1))
    dave_sprite = pygame.transform.scale(dave_sprite, (width * scale, height * scale))
    return dave_sprite
