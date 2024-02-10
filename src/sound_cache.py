import pygame
from pygame.mixer import Sound
import globalvar

pygame.mixer.init()
JUMP = Sound(globalvar.GLOBAL_PATH + "sounds/" + "Jump Small.wav")
JUMP.set_volume(0.5)
JUMP_ALT = Sound(globalvar.GLOBAL_PATH + "sounds/" + "Jump Super.wav")
JUMP_ALT.set_volume(0.5)
HURT = Sound(globalvar.GLOBAL_PATH + "sounds/" + "Warp.wav")
DIE = Sound(globalvar.GLOBAL_PATH + "sounds/" + "Die.wav")
STOMP = Sound(globalvar.GLOBAL_PATH + "sounds/" + "Squish.wav")