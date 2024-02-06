import objects.gameobject as gameobject
import pygame
import globalvar

class Collideable(gameobject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gravity = 0
        self.size = (globalvar.TILE_SIZE, globalvar.TILE_SIZE)
        self.rect = pygame.Rect(0, 0, self.size[0], self.size[1])

    def update(self):
        super().update()

        # find the sector (tilemap) of the object
        self.rect.center = ((self.x + 8) - self.camera_x, (self.y + 8) - self.camera_y)

    def render(self, surface, camera):
        super().render(surface, camera)
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
    pass