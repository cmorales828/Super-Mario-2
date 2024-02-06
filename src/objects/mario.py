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

    def update(self):
        super().update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 2
        if keys[pygame.K_RIGHT]:
            self.x += 2
        if keys[pygame.K_UP]:
            self.y -= 2
        if keys[pygame.K_DOWN]:
            self.y += 2

    def render(self, surface, camera):
        surface.blit(self.sprite, (self.x - self.camera_x, self.y - self.camera_y))
        super().render(surface, camera)
        return
    pass
