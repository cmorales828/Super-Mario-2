# this class only exists to be used as a check for enemies
from objects.parents.alt_collideable import AltCollider

# I can't believe these enemies are so STUPID
class Enemy(AltCollider):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_phaseable = True
        self.is_harmful = True

    def kill(self):
        self.flag_for_deletion()

    def flag_for_deletion(self):
        self.dead = True
        self.delete = True