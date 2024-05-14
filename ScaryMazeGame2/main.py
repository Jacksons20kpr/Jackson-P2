#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys
import interface.game
import interface.intro
import interface.outro
pygame.init()
#test
# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

#Setup of Starting objects
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
interface.intro.output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window)
interface.game.output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window)
interface.outro.output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window)