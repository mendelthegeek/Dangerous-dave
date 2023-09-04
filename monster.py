import os

import pygame


class Mobs(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        path = r"resources\dave\death"
        images = os.listdir(path)
        self.death_images = [pygame.image.load(path + "\\" + image) for image in images]

    def render_image(self, sprite):
        sprite.pos = pygame.math.Vector2(sprite.rect.center)
        current_time = pygame.time.get_ticks()
        if sprite.dying:
            if current_time - sprite.last_update > 200:
                sprite.death_frame += 1
                sprite.last_update = current_time
                if sprite.death_frame == 7:
                    self.remove(sprite)
            return self.death_surface(self.death_images[sprite.death_frame]), sprite.rect
        if current_time - sprite.last_update > sprite.speed:
            sprite.update()
            sprite.last_update = current_time
            sprite.image_index += 1
            sprite.set_frame()
        return sprite.image, sprite.rect

    def death_surface(self, death_image):
        surface = pygame.Surface((49, 41)).convert_alpha()
        rectangle = (0, 0, 49, 41)
        surface.blit(death_image, (0, 0), rectangle)
        surface = pygame.transform.scale(surface, (35, 30))
        surface.set_colorkey((0, 0, 0))
        return surface


class Mob(pygame.sprite.Sprite):

    def __init__(self, waypoints, group):
        super().__init__()
        self.x = waypoints[1][0]
        self.y = waypoints[1][1]
        self.vel = pygame.math.Vector2(0, 0)
        self.max_speed = 1.75
        self.pos = pygame.math.Vector2((self.x, self.y))
        self.rect = pygame.Rect((*self.pos, 54, 30))
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.target = self.waypoints[self.waypoint_index]
        self.target_radius = 50
        group.add(self)
        self.last_update = pygame.time.get_ticks()
        self.speed = 5
        self.value = 100
        self.image_index = 1
        self.set_frame()

        self.dying = False
        self.death_frame = -1

        self.bullet = None

    def update(self):
        self.target = self.waypoints[self.waypoint_index]
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
            self.vel = heading * (distance / self.target_radius)**.25 * self.max_speed
        else:  # Otherwise move with max_speed.
            self.vel = heading * self.max_speed

        self.pos += self.vel
        self.rect.center = self.pos

    def set_frame(self):
        self.image = pygame.Surface((81, 45)).convert_alpha()
        picture = pygame.image.load(r"resources/mobs/spider"
                                    f"{(self.image_index//25)%3+1}"
                                    r".png")
        self.image.blit(picture, (0, 0))
        self.image = pygame.transform.scale(self.image, (54, 30))
        self.image.set_colorkey((0, 0, 0))


    def die(self):
        self.dying = True
