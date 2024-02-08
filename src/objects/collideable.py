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

    def update_center(self):
        self.rect.center = (self.x + self.offset_x, self.y + self.offset_y)

    # Collision Functions and Helper functions
    '''
        The purpose of these functions is to provide each extension of this class
        with an interface that allows them to change their behavior with other classes minimally;
        The player class will be able to null collisions when they are colliding with enemies, for example
        or have exceptions and edge cases where they should do something else upon collision instead.

        The "collide" functions allow an interface to the actual collision detection, 
        whereas the bump functions allow access to what happens when the collision is actually made
    '''
    def wall_collide(self, collision, raw_object):
        change_x = self.x - self.prev_x
        dir_sign = math.copysign(1, collision.centerx - self.x)
        if dir_sign == math.copysign(1, change_x):
            if self.rect.colliderect(collision):
                while self.rect.colliderect(collision):
                    self.bump_wall(collision)
                    self.x -= dir_sign
                    self.update_center()
    
    def floor_collide(self, collision, raw_object):
        # floor collisions
        if self.rect.colliderect(collision) \
        and self.y < collision.top \
        and (collision.top <= self.rect.bottom + 1):
            # push upwards if not on ground
            while (collision.top < self.rect.bottom):
                self.y -= 1
                self.update_center()
            # else on ground
            self.bump_floor(collision)
            return True
        elif self.rect.bottom == collision.top:
            self.bump_floor(collision)
            return True
        return False
    
    def ceiling_collide(self, collision, raw_object):
        while self.rect.colliderect(collision) \
        and self.y + self.offset_y > collision.bottom \
        and self.rect.top < collision.bottom:
            self.y += 1
            self.bump_ceil(collision)
            self.update_center()

    # Bump functions to allow you to bump into things you IDIOT
    def bump_wall(self, wall):
        self.vel_x = 0
    
    def bump_floor(self, floor):
        self.vel_y = 0

    def bump_ceil(self, ceil):
        self.vel_y = 0

    # UPDATE PHYSICS
    def physics_update(self):
        self.prev_x = self.x
        self.prev_y = self.y
 
        if not self.ground:
            self.vel_y += self.gravity
        # apply physics speeds
        self.vel_y = min(self.vel_y, 4)

        self.x += self.vel_x
        self.y += self.vel_y

    # UPDATE THE ACTUAL OBJECT
    def update(self, map, objects):
        super().update()
        self.update_center()

        # find the sector (tilemap) of the object
        map_collisions = []
        for i in map.tilemaps: # check if colliding with general sector 
            if self.rect.colliderect(i.rect):
                for collision in i.collision_map:
                    map_collisions.append(collision)
        # to avoid doing a typecast we store these in an alternate array because FUCK typecasting god damn it its so fucking expensive
        object_collisions = []
        for i in objects:
            if i != self and isinstance(i, Collideable):
                object_collisions.append(i) # append the raw object
        all_collisions = (map_collisions, object_collisions)

        change_x = self.x - self.prev_x
        change_y = self.y - self.prev_y

        self.ground = False
        for collision_attempt in range(len(all_collisions)):
            for i in all_collisions[collision_attempt]:
                raw_object = i # set the raw object to this stupid thing
                collision = raw_object # assume this is a case where they are the same thing
                if collision_attempt == 1:
                    collision = raw_object.rect # JUST KIDDING ITS NOT

                self.x -= change_x
                self.update_center()
                # vertical collisions
                if (self.rect.right > collision.left or self.rect.left < collision.right) \
                and (self.rect.left < collision.right and self.rect.right > collision.left):
                    # ceiling collisions
                    self.ceiling_collide(collision, raw_object)

                    temp_ground = self.floor_collide(collision, raw_object)
                    if temp_ground:
                        self.ground = temp_ground

                self.x += change_x
                self.update_center()
                
                # wall collisions
                self.y -= change_y
                self.update_center()

                self.wall_collide(collision, raw_object)

                self.y += change_y
                self.update_center()

    def render(self, surface, camera):
        super().render(surface, camera)
    pass