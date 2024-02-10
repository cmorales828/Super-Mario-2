import objects.gameobject as gameobject
import globalvar 

class Camera(gameobject.GameObject):
    def __init__(self, x, y, surface):
        super().__init__(x, y)
        self.following = -1
        self.width = (surface.get_width() // globalvar.ZOOM)
        
    def update(self):
        if self.following != -1:
            self.x = (self.following.x + 8) - (self.width // 2)
            # self.y = (self.following.y + 8) - ((surface.get_height() // globalvar.ZOOM) // 2)  

    def render():
        return