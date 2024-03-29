import pygame
import math
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # camera stuff
        self.camera_x = 0
        self.camera_y = 0

        # collision and globals
        self.rect = -1
        self.is_player = False
        self.is_phaseable = False
        self.is_collideable = False
        self.is_harmful = False
        self.is_block = False
        self.dead = False

        self.delete = False
        self.draw = True

    def physics_update(self):
        return

    def update(self, map, objects):
        return

    def render(self, surface, camera):
        # do camera calculations
        if camera != -1:
            self.camera_x = math.floor(camera.x)
            self.camera_y = math.floor(camera.y)
        return
    
def create_object(x, y):
    return GameObject(x, y)