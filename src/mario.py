import gameobject
import globalvar
import pygame

# Mario Object
class Mario(gameobject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        # Define temp sprite
        self.temp_sprite = globalvar.GLOBAL_PATH + "tile/tile1.png"
        self.sprite = pygame.image.load(self.temp_sprite)

    def render(self, surface):
        surface.blit(self.sprite, (self.x, self.y))
        return
    pass
