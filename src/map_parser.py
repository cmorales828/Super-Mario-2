import objects.tilemap as tilemap
import objects.gameobject as gameobject

class Map(gameobject.GameObject):
    def __init__(self, path="0.txt"):
        my_tilemap = tilemap.Tilemap()
        