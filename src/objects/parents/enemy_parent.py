# this class only exists to be used as a check for enemies
from objects.collideable import Collideable
from objects.parents.player_parent import Player

# I can't believe these enemies are so STUPID
class Enemy(Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_phaseable = True

    def ceiling_collide(self, gameobject):
        if not gameobject.is_player \
        and not (gameobject.is_phaseable and (gameobject.dead or self.dead)):
            return super().ceiling_collide(gameobject)
        return False

    def wall_collide(self, gameobject):
        if not gameobject.is_player \
        and not (gameobject.is_phaseable and (gameobject.dead or self.dead)):
            return super().wall_collide(gameobject)
        return False
    
    def floor_collide(self, gameobject):
        if not gameobject.is_player \
        and not (gameobject.is_phaseable and (gameobject.dead or self.dead)):
            return super().floor_collide(gameobject)
        return False
    
    def kill(self):
        self.flag_for_deletion()

    def flag_for_deletion(self):
        self.dead = True
        self.delete = True