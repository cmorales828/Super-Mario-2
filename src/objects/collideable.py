import objects.gameobject as gameobject
import pygame
import globalvar

class Collideable(gameobject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gravity = 0
        self.size = (globalvar.TILE_SIZE, globalvar.TILE_SIZE)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])
        
        self.mask = pygame.mask.Mask((self.rect.width, self.rect.height))
        self.mask.fill()
        self.draw = False

    def update(self, map, objects):
        super().update()

        # update our collision box
        self.rect.center = (self.x, self.y)

        # find the sector (tilemap) of the object
        map_collisions = []
        for i in map.tilemaps: # check if colliding with general sector 
            if self.rect.colliderect(i.rect):
                map_collisions.append(i)

        # for i in map_collisions:
            # if self.mask.overlap(i.mask, (self.x, self.y)):

        # find collision map of individual collided maps

    def render(self, surface, camera):
        super().render(surface, camera)
    pass