import objects.gameobject as gameobject
import globalvar
import pygame

# Mario Object
class Mario(gameobject.GameObject):
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
        super().render(surface, camera)
        surface.blit(self.sprite, (self.x - self.camera_x, self.y - self.camera_y))
        return
    pass
