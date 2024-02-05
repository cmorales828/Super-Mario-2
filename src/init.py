import pygame
import sys

import gameobject

# Init pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Cual Abogado")

clock = pygame.time.Clock()
fps = 60

objects = [gameobject.create_object(200, 200)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle updating objects
    for i in objects:
        i.update_self()

    # clear screen
    screen.fill((0, 0, 0))
    for i in objects:
        i.draw_self(screen)
        
    # update display
    pygame.display.update()
    clock.tick(fps)