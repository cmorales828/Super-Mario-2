import objects.gameobject as gameobject
import pygame
import math
import globalvar
class Collideable(gameobject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        # collision values
        self.gravity = 0.1
        self.ground = False
        self.vel_x = 0
        self.vel_y = 0
        self.dir = 1

        # other values
        self.size = (globalvar.TILE_SIZE, globalvar.TILE_SIZE)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        self.draw = False

    def update_center(self):
        self.rect.center = (self.x, self.y)

    def physics_update(self):
        if not self.ground:
            self.vel_y += self.gravity
    
        # apply physics speeds
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
 
        self.ground = False
        for i in map_collisions:
            for j in self.rect.collidelistall(i.collision_map):
                collision = i.collision_map[j]
                # floor collision
                if collision.top <= self.rect.bottom:
                    self.ground = True
                    while collision.top < self.rect.bottom:
                        self.y -= 1
                        self.update_center()

                self.rect.bottom -= 2

        # find collision map of individual collided maps

    def render(self, surface, camera):
        super().render(surface, camera)
    pass