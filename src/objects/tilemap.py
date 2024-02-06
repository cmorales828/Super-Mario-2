import numpy as np
import objects.gameobject as gameobject

class Tilemap(gameobject.GameObject): 
    def __init__(self, texture_name="tile/tile1", size=(16, 16)):
        self.size = size
        self.map = []
        print(self.map)
    
    def render(self, surface):
        super().render(surface)