import globalvar
import pygame
import objects.collideable as collideable

# Mario Object
class Mario(collideable.Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)
        # Define temp sprite
        self.temp_sprite = globalvar.GLOBAL_PATH + "tile/tile1.png"
        self.sprite = pygame.image.load(self.temp_sprite)

    def update(self, map, objects):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2

        super().update(map, objects)

    def render(self, surface, camera):
        super().render(surface, camera)
        surface.blit(self.sprite, ((self.x - self.size[0] / 2) - self.camera_x, (self.y - self.size[1] / 2) - self.camera_y))
        if (self.ground):
            pygame.draw.rect(surface, (255, 255, 255), self.rect)
    pass
