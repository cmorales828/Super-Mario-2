import pygame
import sys

import math

import globalvar
import gameobject
import mario

# Init pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
f_screen = pygame.Surface(size=(screen.get_width() // 2, screen.get_height() // 2))
pygame.display.set_caption("Cual Abogado")

clock = pygame.time.Clock()
fps = 60

objects = []
for i in range(16):
    objects.append(mario.Mario(100 + i * 16, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle updating objects
    for i in objects:
        i.x += 1
        if i.x > screen.get_width() // 2:
            i.x -= (screen.get_width() // 2 + 16)
        i.y = 100 + math.sin(i.x / 100 + (pygame.time.get_ticks() / 1000)) * (screen.get_height() // 8)
        i.update()

    # clear screen
    f_screen.fill((0, 0, 0))
    for i in objects:
        i.render(f_screen)
        
    # update display
        
    # psuedosurface stuff (displaying at 2x size)
    f_screen = pygame.transform.scale_by(f_screen, globalvar.ZOOM)
    screen.blit(f_screen, (0, 0))
    f_screen = pygame.transform.scale_by(f_screen, 1 / globalvar.ZOOM)

    # update surface
    pygame.display.update()
    clock.tick(fps)