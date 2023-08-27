import pygame


class Mobs(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def render_image(self, sprite):
        current_time = pygame.time.get_ticks()
        if current_time - sprite.last_update > sprite.speed:
            sprite.update()
            sprite.last_update = current_time
        return sprite.image, sprite.pos


class Mob(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y, waypoints, group):
        super().__init__()
        self.x = start_x
        self.y = start_y
        self.image = pygame.Surface((81, 45)).convert_alpha()
        picture = pygame.image.load(r"resources/mobs/spider1_new.png")
        self.image.blit(picture, (0, 0))
        self.image = pygame.transform.scale(self.image, (54, 30))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.vel = pygame.math.Vector2(0, 0)
        self.max_speed = 3
        self.pos = pygame.math.Vector2((start_x, start_y))
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 50
        group.add(self)
        self.last_update = pygame.time.get_ticks()
        self.speed = 5

    def update(self):
        # A vector pointing from self to the target.
        heading = self.target - self.pos
        distance = heading.length()  # Distance to the target.
        heading.normalize_ip()
        if distance <= 2:  # We're closer than 2 pixels.
            # Increment the waypoint index to switch the target.
            # The modulo sets the index back to 0 if it's equal to the length.
            self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
            self.target = self.waypoints[self.waypoint_index]
        if distance <= self.target_radius:
            # If we're approaching the target, we slow down.
            self.vel = heading * (distance / self.target_radius * self.max_speed)
        else:  # Otherwise move with max_speed.
            self.vel = heading * self.max_speed

        self.pos += self.vel
        self.rect.center = self.pos