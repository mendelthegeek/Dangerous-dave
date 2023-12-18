import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, direction: int, creature: str, x: int = 0, y: int = 0) -> None:
        super().__init__()
        self.x: int = x + (direction + 1) * 10
        self.y: int = y + 10
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, 18, 6)
        self.x_dir: int = direction
        self.last_updated: int = pygame.time.get_ticks()
        if creature == "dave":
            self.image: pygame.Surface = pygame.image.load("resources/dave/bullet.png")
        elif creature == "mob":
            self.image: pygame.Surface = pygame.image.load("resources/mobs/bullet.png")

    def move(self) -> None:
        curr_ticks: int = pygame.time.get_ticks()
        if curr_ticks - self.last_updated > 3:
            self.x += self.x_dir
            self.last_updated = curr_ticks
        self.rect.update(self.x, self.y, 18, 6)

    def get_location(self) -> (pygame.Surface, tuple[int, int]):
        image = self.image
        if self.x_dir == -1:
            image = pygame.transform.flip(self.image, True, False)
        image = pygame.transform.scale(image, (2 * image.get_width() // 3, 6))
        image.set_colorkey((0, 0, 0))
        return image, (self.x, self.y)
