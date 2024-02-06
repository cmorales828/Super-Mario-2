import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        return

    def render(self, surface):
        return
    
def create_object(x, y):
    return GameObject(x, y)