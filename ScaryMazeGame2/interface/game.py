#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys
import interface.game
import Objects.moving
import Objects.image
import global_vars
from pygame import mixer
mixer.init() 



def play_music(file_path, volume=1.0):
    mixer.music.load(file_path)
    mixer.music.set_volume(volume)
    mixer.music.play()
    
    
 
def output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window):
    global show
    show = False
    red = Objects.moving.Person(150,160,35,25,"images/red.png")
    maze = Objects.image.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,"images/Maze.png")
    scary = Objects.image.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,"images/scary.png")
    arrow = Objects.image.still(890,840,40,70,"images/arrow.png")
    pygame.display.set_caption(f"Welcome{global_vars.name}")
    
    def next():
        global done 
        done=True

    def display():
        global show
        window.fill((0,0,0))
        arrow.draw(window)
        maze.draw(window)
        red.draw(window)
        if pygame.sprite.collide_mask(red, maze):
            show = True 
            play_music("images/Scream.mp3")
        if show==True:
            scary.draw(window) 
        
        
           
            
        
            
        #circle=pygame.draw.circle(window,(54, 221, 255),(circle_x,250),30)
        

    # def collision(img_scary, walls):
    #     return img_scary.colliderect(walls)
    def collision(object1, object2):
        return object1.colliderect(object2)

    done = False
    while not done:
        red.move(5)
        display()
        if pygame.sprite.collide_mask(red, maze):   
            red.move_back()
        display()
        if pygame.sprite.collide_mask(red,arrow):
            done=True

        for event in pygame.event.get():
                # if user  QUIT then the screen will close
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
    
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    