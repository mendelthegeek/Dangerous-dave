from render import *


class Dave(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x, self.y = 64, 338
        self.sprite_source = r"resources\dave\Dave.png"

        self.speed = 8

        self.sprite_sheet = SpriteSheet(self)
        self.jump_height = 0

        self.walk_right = []
        for i in range(4):
            self.walk_right.append(self.sprite_sheet.get_sprite(0, i, 24, 16, 2))
        self.display_frame = self.walk_right[0]
        self.walk_left = []
        for i in range(4):
            self.walk_left.append(self.sprite_sheet.get_sprite(1, i, 24, 16, 2))
        self.x_speed = 0
        self.y_speed = 0
        self.facing = 0
        self.moved = False
        self.displayed = True
        self.on_surface = False
        self.last_blinked = pygame.time.get_ticks()
        self.rect = pygame.Rect(0,0,0,0)
        self.move()
        self.last_update = pygame.time.get_ticks()

    def current_display(self):
        if not self.x_speed == 0:
            # expression maps 1 to 0 and -1 to 1, mapping movement to desired spritesheet row
            self.facing = (1 - self.x_speed)/2
        if not self.moved:
            current_ticks = pygame.time.get_ticks()
            if current_ticks - self.last_blinked > 500:
                self.last_blinked = current_ticks
                self.displayed = not self.displayed
            if self.displayed:
                empty_square = (pygame.Surface((24, 16)))
                empty_square.fill(BG)
                return empty_square
            elif not self.displayed:
                return self.sprite_sheet.get_sprite(0, 6, 24, 16, 2)
        if self.on_surface:
            return self.sprite_sheet.get_sprite(self.facing, self.sprite_sheet.frame//8 % 4, 24, 16, 2)
        else:
            return self.sprite_sheet.get_sprite(self.facing,5,24, 16, 2)

    def position(self):
        return self.x, self.y

    def move(self):
        if not self.x_speed == 0 or not self.y_speed == 0:
            self.moved = True
        if not self.x_speed == 0:
            self.sprite_sheet.move_frame()
        self.jump()
        self.x += self.x_speed
        self.y += self.y_speed
        self.move_rect()

    def jump(self):
        if self.jump_height == 0 and self.moved:
            if not self.on_surface:
                self.y_speed = 1
            else:
                self.y_speed = 0
        if self.jump_height > 0:
            self.jump_height -= 1
            if self.jump_height > 11:
                self.y_speed = -1
            else:
                self.y_speed = 0

    def move_rect(self):
        self.rect.update(self.x, self.y, 20, 32)
