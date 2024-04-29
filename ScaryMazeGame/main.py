#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys


pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

#Setup of Starting objects
circle_x=0
img_red = pygame.image.load('red.png') #with .png or .jpb included in the name
img_red = pygame.transform.scale(img_red, (35, 35))  #resize image Where 35 ,35 is the size, (x,y)
red_y = 150
red_x = 150
speed = 2
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("Scary Maze Game")
def display():
    global walls,red
    walls=[]
    window.fill((0,0,0)) #White background
    walls.append(pygame.draw.rect(window,(54, 221, 255),(0,WINDOW_HEIGHT-10,WINDOW_WIDTH,10)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(0,0,WINDOW_WIDTH,10)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(0,0,10,WINDOW_HEIGHT)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(WINDOW_WIDTH-10,0,10,WINDOW_HEIGHT)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(WINDOW_WIDTH-250,WINDOW_HEIGHT-100,50,100)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(WINDOW_WIDTH-WINDOW_WIDTH+50,WINDOW_HEIGHT-100,700,40)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(WINDOW_WIDTH-WINDOW_WIDTH+50,WINDOW_HEIGHT-100-55,50,55)))
    walls.append(pygame.draw.rect(window,(54, 221, 255),(WINDOW_WIDTH-WINDOW_WIDTH+50,WINDOW_HEIGHT-200-55,50,55)))

    #circle=pygame.draw.circle(window,(54, 221, 255),(circle_x,250),30)
    red=window.blit(img_red,(red_x, red_y))

# def collision(img_scary, walls):
#     return img_scary.colliderect(walls)
def collision(object1, object2):
    return object1.colliderect(object2)


while True:
    global red
    #value name---pygame check if keys down---->Create a variable that is set to all the key values
    key_input = pygame.key.get_pressed()

 
    #var--------value name-----key Left---speed value--value name------key Right---speed value      
    movex = (key_input[pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
    movey = (key_input[pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)

    #x-location + x-speed = new x-location
    red_x += movex

    #y-location + y-speed = new y-location
    red_y += movey
    display()
    circle_x+=10
    if circle_x > WINDOW_WIDTH:
        circle_x=0
    
    for wall in walls:
        if collision(red,wall):
            red_x -= movex
            red_y -= movey
            display()
  

    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw