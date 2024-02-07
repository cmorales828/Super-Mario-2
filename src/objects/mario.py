import globalvar
import pygame
import math
import objects.collideable as collideable
from map_parser import Tileset

# Mario Object
class Mario(collideable.Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)

        # gravity base
        self.gravity_base = 0.4
        self.gravity_alt = 0.1

        self.gravity = self.gravity_base
        
        self.acc = 0.05
        self.accskid = 0.125
        self.deccel = 0.1
        self.deccskid = 0.05
        
        self.jumpstr = 3.85
        self.vel_x_max = 2.5

        self.image_index = 0
        self.jumping = 0
        # sprites
        self.super_mario = Tileset("player/big_mario.png", 16, 32)
        self.current_sprite = self.super_mario
        self.rect = self.current_sprite.get(self.image_index).get_rect()
        self.offset_y += 8
        print(self.rect)

    def update(self, map, objects):
        keys = pygame.key.get_pressed()
        keys_pressed = pygame.key.get_just_pressed()

        move = keys[pygame.K_d] - keys[pygame.K_a]
        sign_of = math.copysign(1, move)
        if abs(move) > 0:
            if sign_of == math.copysign(1, self.vel_x):
                self.vel_x += move * self.acc
                self.dir = sign_of
            else:
                self.vel_x += move * self.accskid
        else: # decceleration
            self.vel_x = max(0, abs(self.vel_x) - self.deccel) * math.copysign(1, self.vel_x)
            if self.vel_x < self.deccel and self.vel_x > -self.deccel:
                self.vel_x = 0
        self.vel_x = max(-self.vel_x_max, min(self.vel_x, self.vel_x_max))

        super().update(map, objects)

        if self.ground \
        and keys_pressed[pygame.K_SPACE]:
            self.ground = False
            self.vel_y = -(self.jumpstr + (abs(self.vel_x) / 7.5))
            self.jumping = 1

        if self.jumping >= 1 and not self.ground:
            if self.jumping == 1 and self.vel_y < -1:
                self.jumping = (not keys[pygame.K_SPACE]) + 1
                self.gravity = self.gravity_alt
            else:
                self.jumping = 2
                self.gravity = self.gravity_base
        else: self.jumping = 0

        # animation control
        if self.jumping == 0 or self.ground:
            if abs(move) > 0:
                self.image_index += 0.1
                if self.image_index > 4:
                    self.image_index -= 3
            else:
                self.image_index = 0
        else:
            self.image_index = 5

    def render(self, surface, camera):
        super().render(surface, camera)
        cur_sprite_copy = self.current_sprite.get(self.image_index).copy()
        cur_sprite_copy = pygame.transform.flip(cur_sprite_copy, self.dir == -1, False)
        surface.blit(cur_sprite_copy, ((self.x - self.size[0] / 2) - self.camera_x, (self.y - self.size[1] / 2) - self.camera_y))
    pass
