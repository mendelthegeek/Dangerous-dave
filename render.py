import pygame

BG = (50, 50, 50)

board = pygame.display.set_mode((1200, 700))


def test_render(dave, tiles, last_update):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    if current_time - last_update > dave.speed:
        dave.move()
        last_update = current_time
    board.blit(dave.current_display(), dave.position())
    for i in range(10):
        for j in range(4):
            board.blit(tiles.tile(), (i * 32 +j*128, 668 - j*96))
    pygame.display.flip()
    return last_update


class SpriteSheet:

    def __init__(self, sprite):
        self.sprite = sprite
        self.sprite_sheet = pygame.image.load(self.sprite.sprite_source)
        self.frame = 0

    def get_sprite(self, row, column, width, height, scale):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite_rectangle = ((column * (width + 1)) + 1, 1 + row * (height + 1), (1 + width * (column + 1)), (height + 1) * (row + 1))
        sprite.blit(self.sprite_sheet, (0, 0), sprite_rectangle)
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite.set_colorkey((0, 0, 0))
        return sprite

    def move_sprite(self, x, y):
        self.sprite.x += x
        self.sprite.y += y

    def move_frame(self):
        self.frame += 1
