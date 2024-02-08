from objects.collideable import Collideable

# this class only exists to be used as a check for enemies
class Enemy(Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)