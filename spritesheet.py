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
