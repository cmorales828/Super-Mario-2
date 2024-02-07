import objects.gameobject as gameobject
import pygame
import math
import globalvar

class Collideable(gameobject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        # collision values
        self.gravity = 0
        self.ground = False

        self.offset_x = 0
        self.offset_y = 0

        self.vel_x = 0
        self.vel_y = 0
        self.dir = 1

        self.prev_x = x
        self.prev_y = y

        # other values
        self.size = (globalvar.TILE_SIZE, globalvar.TILE_SIZE)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.draw = False

    def update_center(self):
        self.rect.center = (self.x + self.offset_x, self.y + self.offset_y)

    def physics_update(self):
        self.prev_x = self.x
        self.prev_y = self.y
 
        if not self.ground:
            self.vel_y += self.gravity
        # apply physics speeds
        self.vel_y = min(self.vel_y, 4)

        self.x += self.vel_x
        self.y += self.vel_y

    def update(self, map, objects):
        super().update()
        self.update_center()

        # find the sector (tilemap) of the object
        map_collisions = []
        for i in map.tilemaps: # check if colliding with general sector 
            if self.rect.colliderect(i.rect):
                map_collisions.append(i)

        change_x = self.x - self.prev_x
        change_y = self.y - self.prev_y

        grounded = False
        for i in map_collisions:
            for collision in i.collision_map:
                self.x -= change_x
                self.update_center()
                # vertical collisions
                if (self.rect.right > collision.left + 1 or self.rect.left < collision.right - 1) \
                and (self.rect.left < collision.right and self.rect.right > collision.left):
                    # ceiling collisions
                    while self.rect.colliderect(collision) \
                    and self.y > collision.bottom \
                    and self.rect.top < collision.bottom:
                        self.y += 1
                        self.update_center()

                    # floor collisions
                    if self.rect.colliderect(collision) \
                    and self.y < collision.top \
                    and (collision.top <= self.rect.bottom + 1):
                        # push upwards if not on ground
                        while (collision.top < self.rect.bottom):
                            self.y -= 1
                            self.update_center()
                        # else on ground
                        self.vel_y = 0
                        grounded = True
                    elif self.rect.bottom == collision.top:
                        self.vel_y = 0
                        grounded = True

                self.x += change_x
                self.update_center()
                
                # wall collisions
                self.y -= change_y
                self.update_center()
                dir_sign = math.copysign(1, collision.centerx - self.x)
                if dir_sign == math.copysign(1, change_x):
                    if self.rect.bottom <= collision.bottom or self.rect.top >= collision.top:
                        while self.rect.colliderect(collision):
                            self.vel_x = 0
                            self.x -= dir_sign
                            self.update_center()
                self.y += change_y
                self.update_center()
        self.ground = grounded

    def render(self, surface, camera):
        super().render(surface, camera)
    pass