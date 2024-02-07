import pygame
import math
import objects.gameobject as gameobject
import globalvar

# Class for tilesets, that contain all tile information
class Tileset:
    def __init__(self, file_name, width = globalvar.TILE_SIZE, height = globalvar.TILE_SIZE):
        self.image = pygame.image.load(globalvar.GLOBAL_PATH + file_name)
        self.rect = self.image.get_rect()
        # load tileset
        self.tiles = []
        for x in range(self.rect.width // width):
            for y in range(self.rect.height // height):
                temp_size = (width, height)
                tile = pygame.Surface(temp_size)
                tile.blit(self.image, (0, 0), (x * width, y * height, *temp_size))
                self.tiles.append(tile)
    
    def get(self, index):
        return self.tiles[math.floor(index) % len(self.tiles)]

# Tilemaps are subdivisions of maps that are 16 x 16, containing that many tiles within them
class Tilemap(gameobject.GameObject): 
    def __init__(self, x=0, y=0, tilemap_width=16, tilemap_height=16):
        self.x = x
        self.y = y
        self.surface = pygame.Surface(size=(globalvar.TILE_SIZE * tilemap_width, globalvar.TILE_SIZE * tilemap_height))
        # get current rectangle for total tilemap collision
        self.collision_map = []
        self.rect = self.surface.get_rect()
        self.rect.x += self.x
        self.rect.y += self.y

    def render(self, surface, camera):
        super().render(surface, camera)
        surface.blit(self.surface, (math.floor(self.x) - self.camera_x, math.floor(self.y) - self.camera_y))
        # for i in self.collision_map:
        #     pygame.draw.rect(surface, (255, 255, 255), i)
    pass

# The map class creates the current loaded map
class Map(gameobject.GameObject):
    def __init__(self, path="0.txt"):
        f = open(globalvar.MAP_PATH + path, "r")
        # get the information from the txt file (current format for maps)
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
                # If you wanted to add tiles/objects, this would be the place to do it
                if not "0" in cur_tile and not " " in cur_tile:
                    index = 0
                    try:
                        index = int(cur_tile) - 1
                        cur_tilemap.collision_map.append(pygame.Rect(cur_tilemap.x + (size_i * globalvar.TILE_SIZE), cur_tilemap.y + (j * globalvar.TILE_SIZE), globalvar.TILE_SIZE, globalvar.TILE_SIZE))
                        cur_tilemap.surface.blit(tileset.tiles[index], (size_i * globalvar.TILE_SIZE, j * globalvar.TILE_SIZE))
                    except ValueError:
                        # create object instead if not value
                        continue
            size_i += 1
            i += 1
            if size_i > size_limit - 1 or i == tilemap_width - 1: 
                size_i = 0

    def render(self, surf, camera):
        super().render(surf, camera)
        for i in self.tilemaps:
            i.render(surf, camera)
    pass