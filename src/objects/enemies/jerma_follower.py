import math
import random
import pygame
import globalvar
from objects.enemies.goomba import Goomba

class Jerma(Goomba):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image = pygame.image.load(globalvar.GLOBAL_PATH + "enemies/jermafollower.png")
        temp_size = (self.image.get_width(), self.image.get_height())
        self.tile = pygame.Surface(temp_size)
        self.tile.fill(globalvar.COLOR_MASK)
        self.tile.blit(self.image, (0, 0))
        self.tile.set_colorkey(globalvar.COLOR_MASK)
        self.tile = pygame.transform.scale_by(self.tile, (10 / random.randrange(30, 100, 1)))
        self.size = (self.tile.get_width(), self.tile.get_height())
        self.rect = self.tile.get_rect()
        self.rect.center = (self.x, self.y)

        self.current_sprite = -1
        self.dir = 1
        self.vel_x = 0

    def update(self, map, objects):

        self.dir -= 0.1
        if self.dir < -2:
            self.dir = 0
        if not self.dead:
            self.vel_x -= math.copysign(0.05, self.x - objects[0].x)
            self.vel_x = max(min(self.vel_x, 5), -5)
            super().update(map, objects)

    def kill(self):
        self.ground = False
        self.vel_y -= 1
        super().kill()

    def render(self, surface, camera):
        super().render(surface, camera)
        cur_sprite_copy = self.tile.copy()
        cur_sprite_copy = pygame.transform.flip(cur_sprite_copy, self.dir <= -1, False)
        surface.blit(cur_sprite_copy, (math.floor(self.x - self.size[0] / 2) - self.camera_x, math.floor(self.y - self.size[1] / 2) - self.camera_y))
    pass