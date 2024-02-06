import pygame
import sys
import math

import globalvar
import map_parser
import objects.collideable as collideable

import objects.camera as camera
import objects.mario as mario

# Init pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
f_screen = pygame.Surface(size=(screen.get_width() // 2, screen.get_height() // 2))
pygame.display.set_caption("Cual Abogado")

clock = pygame.time.Clock()
fps = 60

map = map_parser.Map()
mario_object = mario.Mario(64, 64)
game_camera = camera.Camera(0, 0)
game_camera.following = mario_object
objects = [map, mario_object]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle updating objects
    for i in objects:
        i.update()
    # update camera separately
    game_camera.update(f_screen)

    # clear screen
    f_screen.fill((0, 0, 0))
    for i in objects:
        i.render(f_screen, game_camera)
        
    # psuedosurface stuff (displaying at zoomed size)
    f_screen = pygame.transform.scale_by(f_screen, globalvar.ZOOM)
    screen.blit(f_screen, (0, 0))
    f_screen = pygame.transform.scale_by(f_screen, 1 / globalvar.ZOOM)

    # update surface
    pygame.display.update()
    clock.tick(fps)