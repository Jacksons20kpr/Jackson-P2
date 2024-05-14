import pygame

class no_background(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y, font_name,font_size,text_color,hover_color,text,action):
        super().__init__()
        font_used = pygame.font.SysFont(font_name, font_size)
        self.text_surface = font_used.render(text, True, text_color)
        self.default=self.text_surface
        self.hover_text= font_used.render(text, True, hover_color)
        self.image=self.text_surface
        self.hover = self.hover_text
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
   
        self.action = action

    def update(self,pos,event):              
        if self.rect.collidepoint(pos):          
            self.image =self.hover
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.action()
        else:
            self.image =self.default
    def draw(self, screen):
        # Render the text surface
       screen.blit(self.image,self.rect)
class with_background(no_background):
    def __init__(self,start_x,start_y,width,height, font_name,font_size,back_color,text_color,hover_color,back_hover_color,text,action):
        super().__init__(start_x,start_y, font_name,font_size,text_color,hover_color,text,action)
        self.text_width=self.text_surface.get_width()
        self.text_height= self.text_surface.get_height()

        self.default = pygame.Surface([width, height],pygame.SRCALPHA).convert_alpha()
        self.default.fill(back_color)  
        self.default.blit(self.text_surface, (((width-self.text_width)/2), ((height-self.text_height)/2)))
       
        self.hover = pygame.Surface([width, height],pygame.SRCALPHA).convert_alpha()
        self.hover.fill(back_hover_color)
        self.hover.blit(self.hover_text, (((width-self.text_width)/2), ((height-self.text_height)/2)))
       
        self.image=self.default
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
               
   
       
class with_images(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,width, height, image_no, image_hover,action):
        super().__init__()        
        self.img_default = pygame.image.load(image_no)
        self.img_hover = pygame.image.load(image_hover)
       
        self.img_default = pygame.transform.scale(self.img_default , (width, height)).convert_alpha()
        self.img_hover = pygame.transform.scale(self.img_hover , (width, height)).convert_alpha()
       
        self.image = self.img_default
        self.mask  = pygame.mask.from_surface(self.image)
   
        self.rect = self.image.get_rect(topleft =(start_x,start_y))
       
        self.action = action

    def update(self,pos,event):              
        if self.check_mouse_collision(pos):
            self.image = self.img_hover
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
               self.action()
        else:
            self.image =self.img_default

    def check_mouse_collision(sprite, mouse_pos):
        mouse_sprite = pygame.sprite.Sprite()
        mouse_sprite.image = pygame.Surface([1, 1])
        mouse_sprite.rect = mouse_sprite.image.get_rect(topleft =mouse_pos)
        return pygame.sprite.collide_mask(sprite, mouse_sprite)
    def draw(self, screen):
        # Render the text surface
       screen.blit(self.image,self.rect)