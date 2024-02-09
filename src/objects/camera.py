import objects.gameobject as gameobject
import globalvar 

class Camera(gameobject.GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.following = -1
    
    def update(self, surface):
        if self.following != -1:
            self.x = (self.following.x + 8) - ((surface.get_width() // globalvar.ZOOM) // 2)
            # self.y = (self.following.y + 8) - ((surface.get_height() // globalvar.ZOOM) // 2)  

    def render():
        return