import pygame

pygame.init()

board = pygame.display.set_mode((500, 500))
dave_sprite_images = pygame.image.load(r"resources\dave\Dave.png")
dave_sprite_images.convert_alpha()


class Dave(pygame.sprite.Sprite):

    def __int__(self):
        self.position = (0, 0)


dave = Dave()
dave.__int__()
# print(dave.position)
BG = (50, 50, 50)


def get_dave_sprite(sheet, width, height, scale):
    dave_sprite = pygame.Surface((width, height)).convert_alpha()
    dave_sprite.blit(dave_sprite_images, (0, 0), ((sheet * (width + 1)) + 1, 1, (1 + width * (sheet + 1)), height + 1))
    dave_sprite = pygame.transform.scale(dave_sprite, (width*scale, height*scale))

    return dave_sprite


run = True
while run:
    board.fill(BG)

    board.blit(get_dave_sprite(0, 24, 16, 2), dave.position)
    board.blit(get_dave_sprite(3, 24, 16, 5), (250, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
