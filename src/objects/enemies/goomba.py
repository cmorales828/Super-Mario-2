import math
import sound_cache
from objects.parents.enemy_parent import Enemy
from objects.tileset import Tileset

class Goomba(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.current_sprite = Tileset("enemies/goomba.png", 16, 16)
        self.vel_x = -0.5
        self.image_index = 0
        self.gravity = 0.1
        self.destroy_timer = 120
    
    def bump_wall(self, wall):
        self.vel_x = -self.vel_x
        if wall.is_collideable:
            wall.vel_x = -wall.vel_x
        return 
    
    def bump_floor(self, floor):
        if abs(self.vel_y) > 1:
            self.vel_y = -(self.vel_y / 2)
            self.y -= 1
        else:
            return super().bump_floor(floor)

    def kill(self):
        self.dead = True
        sound_cache.STOMP.play()
        self.vel_x = 0
        self.gravity = 0.1

    def update(self, map, objects):
        if not self.dead:
            self.image_index += 0.05
            if self.image_index > 2:
                self.image_index = 0
        else:
            self.image_index = 2
            self.destroy_timer -= 1
            if self.destroy_timer <= 0:
                self.flag_for_deletion()
        return super().update(map, objects)
    
    def render(self, surface, camera):
        super().render(surface, camera)
        if self.current_sprite != -1:
            surface.blit(self.current_sprite.get(self.image_index).copy(), (math.floor(self.x - self.size[0] / 2) - self.camera_x, math.floor(self.y - self.size[1] / 2) - self.camera_y))
    pass