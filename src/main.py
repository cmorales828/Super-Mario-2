import pygame
import sys
import math

import globalvar
import map_parser

import objects.camera as camera
import objects.mario as mario

# Init pygame
pygame.init()

scale_res = 3
globalvar.ZOOM = scale_res
alt_res = (256, 224)
modern_res = (420, 240)
cur_res = alt_res
screen = pygame.display.set_mode((cur_res[0] * scale_res, cur_res[1] * scale_res), vsync = 0)
f_screen = pygame.Surface(size=(screen.get_width() // globalvar.ZOOM, screen.get_height() // globalvar.ZOOM))
pygame.display.set_caption("Cual Abogado")

clock = pygame.time.Clock()
fps = 60

mario_object = mario.Mario(64, 64) # The mario object is declared prior to be set as following for the camera
game_camera = camera.Camera(0, 0, screen) # Create the camera as it's an object that must be updated after every other
game_camera.following = mario_object # Set the following object to mario
objects = [mario_object] # Declare all objects (will most likely add objects from map afterwards)
map = map_parser.Map(objects) # The map should not update and is separate from everything else

for_deletion = []

# Instantiate the game loop
while True:
    pygame.display.set_caption("Cual Abogado | {:d} FPS".format(int(clock.get_fps())))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # handle updating objects
    for i in objects:
        # culling check
        if i.x > game_camera.x - game_camera.width * 2 \
        and i.x < game_camera.x + game_camera.width * 2: 
            i.physics_update()
            i.update(map, objects)
        
        # handle deletion
        if i.delete:
            for_deletion.append(i)

    # handle deletion pt. 2
    if len(for_deletion) > 0:
        for i in for_deletion:
            objects.remove(i)
        for_deletion.clear()

    # update camera separately
    game_camera.update()

    # clear screen
    f_screen.fill((148, 148, 255))

    # Render map below everything else
    map.render(f_screen, game_camera)
    for i in objects: # Render objects
        if i.draw:
            i.render(f_screen, game_camera)
    mario_object.render(f_screen, game_camera)
        
    # psuedosurface stuff (displaying at zoomed size)
    f_screen = pygame.transform.scale_by(f_screen, globalvar.ZOOM)
    screen.blit(f_screen, (0, 0))
    f_screen = pygame.transform.scale_by(f_screen, 1 / globalvar.ZOOM)

    # update surface
    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)