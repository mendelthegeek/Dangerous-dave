from player import *

BG = (50, 50, 50)

board = pygame.display.set_mode((500, 500))


def test_render(dave, last_update):
    board.fill(BG)
    current_time  = pygame.time.get_ticks()
    if current_time - last_update > dave.speed:
        dave.move_right()
        last_update = current_time
    board.blit(dave.current_display(), dave.position())
    pygame.display.flip()
    return last_update

class SpriteSheet:

    def __init__(self, source):
        self.sprite_sheet = pygame.image.load(source)
        self.frame = 0

    def get_sprite(self, frame, width, height, scale):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite_rectangle = ((frame * (width + 1)) + 1, 1, (1 + width * (frame + 1)), height + 1)
        sprite.blit(self.sprite_sheet, (0, 0), sprite_rectangle)
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite.set_colorkey((0, 0, 0))
        return sprite

    def move_frame(self):
        self.frame += 1
