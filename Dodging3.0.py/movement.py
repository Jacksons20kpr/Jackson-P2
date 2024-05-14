import pygame
import sys
class Person(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,load_path):
        super().__init__() 
        img_load = pygame.image.load(load_path) 
        self.image = pygame.transform.scale(img_load , (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
    def move_back(self):
        self.rect.x -= self.movex    
        self.rect.y -= self.movey   
    def draw(self,window):
        window.blit(self.image,(self.rect.x, self.rect.y))   
    def move(self,speed):
        #value name---pygame check if keys down---->Create a variable that is set to all the key values
        key_input = pygame.key.get_pressed()

    
        #var--------value name-----key Left---speed value--value name------key Right---speed value      
        self.movex = (key_input[pygame.K_LEFT] * -speed) + (key_input[pygame.K_RIGHT] * speed)
        self.movey = (key_input[pygame.K_UP] * -speed) + (key_input[pygame.K_DOWN] * speed)

        #x-location + x-speed = new x-location
        self.rect.x += self.movex

        #y-location + y-speed = new y-location
        self.rect.y += self.movey