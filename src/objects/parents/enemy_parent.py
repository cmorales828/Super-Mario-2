# this class only exists to be used as a check for enemies
from objects.collideable import Collideable
from objects.parents.player_parent import Player

# I can't believe these enemies are so STUPID
class Enemy(Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dead = False

    def ceiling_collide(self, collision, raw_object):
        if not isinstance(raw_object, Player):
            return super().ceiling_collide(collision, raw_object)
        return False

    def wall_collide(self, collision, raw_object):
        if not isinstance(raw_object, Player):
            return super().wall_collide(collision, raw_object)
        return False
    
    def floor_collide(self, collision, raw_object):
        if not isinstance(raw_object, Player):
            return super().floor_collide(collision, raw_object)
        return False
    
    def kill(self):
        self.flag_for_deletion()

    def flag_for_deletion(self):
        self.dead = True
        self.delete = True