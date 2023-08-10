import pygame

BG = (50, 50, 50)

board = pygame.display.set_mode((640, 334))
board = pygame.display.set_mode((640, 384))


def test_render(dave, tiles, last_update):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    if current_time - last_update > dave.speed:
        dave.move()
        last_update = current_time
    board.blit(dave.current_display(), dave.position())
    board.blit(*tiles.create_tile("horizontal_pipe",(32,288)))
def init_tiles(tiles):
    board.blit(*tiles.create_tile("horizontal_pipe", (32, 338)))
    for j in range(3):
        for i in range(7):
            board.blit(*tiles.create_tile("red_brick", (128 * (j + 1) + i * 32, 306 - j * 64)))
    for j in range(10):
        board.blit(*tiles.create_tile("red_brick", (0, 50 + j * 32)))
    for j in range(10):
        board.blit(*tiles.create_tile("red_brick", (608, 50 + j * 32)))
    for i in range(20):
        board.blit(*tiles.create_tile("red_brick", (i * 32, 50)))
    for i in range(20):
        board.blit(*tiles.create_tile("red_brick", (i * 32, 370)))


def test_render(dave, tiles, curr_score, last_update):
    board.fill(BG)
    current_time = pygame.time.get_ticks()
    if current_time - last_update > dave.speed:
        dave.move()
        last_update = current_time
    board.blit(dave.current_display(), dave.position())
    for tile in tiles.sprites():
        board.blit(tile.image, tile.rect)
    pygame.display.flip()
    return last_update


class SpriteSheet:

    def __init__(self, sprite):
        self.sprite = sprite
        self.sprite_sheet = pygame.image.load(self.sprite.sprite_source)
        self.frame = 0

    def get_sprite(self, row, column, width, height, scale):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite_rectangle = ((column * (width + 1)) + 1, 1 + row * (height + 1), width, height)
        sprite.blit(self.sprite_sheet, (0, 0), sprite_rectangle)
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite.set_colorkey((0, 0, 0))
        return sprite

    def move_sprite(self, x, y):
        self.sprite.x += x
        self.sprite.y += y

    def move_frame(self):
        self.frame += 1
