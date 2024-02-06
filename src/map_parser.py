import pygame
import math
import objects.gameobject as gameobject
import globalvar

class Tileset:
    def __init__(self, file_name):
        self.image = pygame.image.load(globalvar.GLOBAL_PATH + file_name)
        self.rect = self.image.get_rect()

        # load tileset
        self.tiles = []
        for x in range(self.rect.width // globalvar.TILE_SIZE):
            for y in range(self.rect.height // globalvar.TILE_SIZE):
                temp_size = (globalvar.TILE_SIZE, globalvar.TILE_SIZE)
                tile = pygame.Surface(temp_size)
                tile.blit(self.image, (0, 0), (x * globalvar.TILE_SIZE, y * globalvar.TILE_SIZE, *temp_size))
                self.tiles.append(tile)
        print(self.tiles)


class Tilemap(gameobject.GameObject): 
    def __init__(self, x=0, y=0, tilemap_width=16, tilemap_height=16):
        self.x = x
        self.y = y
        self.surface = pygame.Surface(size=(globalvar.TILE_SIZE * tilemap_width, globalvar.TILE_SIZE * tilemap_height))

    def render(self, surface, camera):
        super().render(surface, camera)
        surface.blit(self.surface, (math.floor(self.x - self.camera_x), math.floor(self.y - self.camera_y)))
    pass

class Map(gameobject.GameObject):
    def __init__(self, path="0.txt"):
        f = open(globalvar.MAP_PATH + path, "r")

        temp_array = f.read()
        tilemap_width = temp_array.find("\n")
        tilemap_height = len(temp_array.split("\n")) # probably a better way to do this

        tilemap_array = []
        # print tilemap horizontally
        for i in range(tilemap_width):
            temp_array_height = []
            for j in range(tilemap_height):
                temp_array_height.append(temp_array[i + (j * (tilemap_width + 1))])
            tilemap_array.append(temp_array_height)
        
        self.tilemaps = []
        tileset = Tileset("tile/tile1.png")

        size_limit = 16
        size_i = 0
        i = 0
        cur_tilemap = -1
        while i < tilemap_width:
            if size_i == 0:
                cur_tilemap = Tilemap(i * globalvar.TILE_SIZE, 144, size_limit, tilemap_height)
                self.tilemaps.append(cur_tilemap)
            for j in range(tilemap_height):
                cur_tile = tilemap_array[i][j]
                if not "0" in cur_tile and not " " in cur_tile:
                    index = 0
                    try:
                        index = int(cur_tile) - 1
                        cur_tilemap.surface.blit(tileset.tiles[index], (size_i * globalvar.TILE_SIZE, j * globalvar.TILE_SIZE))
                    except ValueError:
                        # create object instead if not value
                        continue
                    
            size_i += 1
            i += 1
            if size_i > size_limit - 1 or i == tilemap_width - 1: 
                size_i = 0
        print(self.tilemaps)

    def update(self):
        super().update()

    def render(self, surf, camera):
        super().render(surf, camera)
        for i in self.tilemaps:
            i.render(surf, camera)
    pass