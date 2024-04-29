#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys
import interface.game
import Objects.moving
import Objects.image


def output(WINDOW_WIDTH,WINDOW_HEIGHT,fpsClock,fps,window):

    red = Objects.moving.Person(150,160,35,25,"images/red.png")
    maze = Objects.image.still(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,"images/Maze.png")
    pygame.display.set_caption("Scary Maze Game")
    def display():
        window.fill((0,0,0))
        maze.draw(window)
        red.draw(window)

        #circle=pygame.draw.circle(window,(54, 221, 255),(circle_x,250),30)
        

    # def collision(img_scary, walls):
    #     return img_scary.colliderect(walls)
    def collision(object1, object2):
        return object1.colliderect(object2)


    while True:
        red.move(5)
        display()
        if pygame.sprite.collide_mask(red, maze):   
        red.move_back()
        display()

        for event in pygame.event.get():
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    