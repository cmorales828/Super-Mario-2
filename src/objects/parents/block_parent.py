import pygame
from objects.parents.alt_collideable import AltCollider
from objects.tileset import Tileset


class Block(AltCollider):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_block = True
        self.y_start = y
        self.bump = False

        self.current_sprite = Tileset("tile/tile1.png")
        self.image_index = 1
        self.gravity = 0
        self.vel_y = 0
        self.vel_x = 0

    def bump_end(self):
        self.bump = False

    def update(self, map, objects):
        super().update(None, objects)

        if self.bump:
            self.vel_y += 0.25
            if self.y >= self.y_start:
                self.vel_y = 0
                self.y = self.y_start
                self.bump_end()

    def render(self, surface, camera):
        super().render(surface, camera)
        self.current_sprite.draw_self(surface, self.image_index, ((self.x - self.size[0] / 2) - self.camera_x, (self.y - self.size[1] / 2) - self.camera_y), False)