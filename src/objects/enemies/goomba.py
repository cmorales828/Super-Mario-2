import math
from objects.enemies.enemy_parent import Enemy
from objects.tileset import Tileset

class Goomba(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.super_mario = Tileset("enemies/goomba.png", 16, 16)
        self.current_sprite = self.super_mario
        self.vel_x = -0.5
        self.image_index = 0
        self.gravity = 0.1
    
    def bump_wall(self, wall):
        self.vel_x = -self.vel_x
        return 

    def update(self, map, objects):
        self.image_index += 0.05
        if self.image_index > 2:
            self.image_index = 0

        return super().update(map, objects)
    
    def render(self, surface, camera):
        super().render(surface, camera)
        surface.blit(self.current_sprite.get(self.image_index).copy(), (math.floor(self.x - self.size[0] / 2) - self.camera_x, math.floor(self.y - self.size[1] / 2) - self.camera_y))
    pass