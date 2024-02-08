from objects.collideable import Collideable

class Player(Collideable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_player = True