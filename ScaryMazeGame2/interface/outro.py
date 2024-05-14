#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys
import Objects.moving
import Objects.image
import Objects.buttons
import global_vars
import Objects.text
pygame.init()

# Game Setup

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000


def output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window):
    global done
    font = pygame.font.SysFont('Consolas', 30)
    
  
    #btn_next = Objects.buttons.no_background(10,700,"Consolas",40,(240,24,31),(96,24,240),"Yippee! TTTTHHHHEEEE EEEENNNNDDDD!!!!") 
 
    done = False
    while not done:
        window.fill((255,255,255))
        window.blit(font.render("The End!",True, (0,0,0)),(100,250))
        #btn_next.draw(window)
       


        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #btn_next.update(pos,event)
           
             # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            fpsClock = pygame.time.Clock()
            pygame.display.update() #update the display
            fpsClock.tick(fps) #speed of redraw