import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_self(self):
        self.x += 1

    def draw_self(self, surface):
        pygame.draw.polygon(surface=surface, color=(255,255,255),
            points=[
                (self.x - 8, self.y - 8), (self.x + 8, self.y - 8),
                (self.x + 8, self.y + 8), (self.x - 8, self.y + 8)
            ]
        )
    
def create_object(x, y):
    return GameObject(x, y)