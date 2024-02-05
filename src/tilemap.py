import numpy as np
import gameobject

class Tilemap(gameobject.GameObject): 
    def __init__(self, texture_name="tile/tile1", size=(16, 16)):
        self.size = size
        self.map = np.zeros(size, dtype=int)
    
    def render(self, surface):
        super().render(surface)