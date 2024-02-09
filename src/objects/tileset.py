# Class for tilesets, that contain all tile information
import math
import pygame
import globalvar

class Tileset:
    def __init__(self, file_name, width = globalvar.TILE_SIZE, height = globalvar.TILE_SIZE):
        self.image = pygame.image.load(globalvar.GLOBAL_PATH + file_name)
        self.rect = self.image.get_rect()
        self.offset = (0, 0)
        # load tileset
        self.tiles = []
        for y in range(self.rect.height // height):
            for x in range(self.rect.width // width):
                temp_size = (width, height)
                tile = pygame.Surface(temp_size)
                tile.fill(globalvar.COLOR_MASK)
                tile.set_colorkey(globalvar.COLOR_MASK)
                tile.blit(self.image, (0, 0), (x * width, y * height, *temp_size))
                self.tiles.append(tile)
    
    def get(self, index):
        return self.tiles[math.floor(index) % len(self.tiles)]
    
    def draw_self(self, surface, index, coords, flip_x):
        cur_sprite_copy = self.get(index).copy()
        cur_sprite_copy = pygame.transform.flip(cur_sprite_copy, flip_x, False)
        surface.blit(cur_sprite_copy, (coords[0] + self.offset[0], coords[1] + self.offset[1]))