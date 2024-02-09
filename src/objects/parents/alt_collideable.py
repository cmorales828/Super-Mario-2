'''
    This class provides an alternative collider that does not actually interact with the player
    The difference is that objects like enemies and blocks should collide, but should not collide with the player,
    as the player would then push them out of objects and such. 
'''

from objects.collideable import Collideable

class AltCollider(Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)

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
    