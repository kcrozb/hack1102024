"""Testing live share"""
import pygame
import random
import sys
from random import randrange

#initializing constructor
pygame.init()


#screen variables
width= 800
height= 600
start = True
fortnite = 0

trash_x_pos = randrange(width)
trash_y_pos = randrange(height)

#screen resolution
res = (720, 720)

#opens up a window
screen = pygame.display.set_mode((width, height))

# image varibles
background_img = pygame.image.load('images/background.png').convert_alpha()
thanks_img = pygame.image.load('images/thank_you_fish.png').convert_alpha()
dirty_img = pygame.image.load('images/dirty_fish.png').convert_alpha()

# button images
start_img = pygame.image.load('images/start.png').convert_alpha()
crab_img = pygame.image.load('images/crab.png').convert_alpha()
fish_img = pygame.image.load('images/fish.png').convert_alpha()
glass_img = pygame.image.load('images/glass_bottle.png').convert_alpha()
pink_jelly_img = pygame.image.load('images/pink_jelly.png').convert_alpha()
seahorse_img = pygame.image.load('images/seahorse.png').convert_alpha()
soda_img = pygame.image.load('images/soda_can.png').convert_alpha()
tide_img = pygame.image.load('images/tide.png').convert_alpha()
tin_img = pygame.image.load('images/tin.png').convert_alpha()
water_bottle_image = pygame.image.load('images/water_bottle.png').convert_alpha()
restart_img = pygame.image.load('images/new_game.png').convert_alpha()

animals_list = [crab_img, fish_img, pink_jelly_img, seahorse_img]
trash_list = [glass_img, soda_img, tide_img, tin_img, water_bottle_image]

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                print('CLICKED')
                global start 
                start = False
                pygame.time.wait(125)
                
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

class ButtonLitter():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                print('CLICKED')
                global fortnite 
                fortnite = 4
                
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

class ButtonFish():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                print('CLICKED')
                global fortnite 
                fortnite = 1
                
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(300, 300, start_img)
litter_button = ButtonLitter(150, 250, water_bottle_image )
fish_button = ButtonFish(300, 150, fish_img)


def Background_ocean(image):
    size = pygame.transform.scale(image, (width, height))
    screen.blit(size, (0, 0))


text_font = pygame.font.SysFont("Arial", 30)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



def add_trash_at_location(x,y):
    screen.blit(water_bottle_image, (x, y))
    
animals_x_pos = randrange(width)
animals_y_pos = randrange(height)
def add_animal_at_location(x,y):
    screen.blit(pink_jelly_img, (x,y))


# game loop

run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if start == True:
        print(fortnite)
        Background_ocean(background_img)
        draw_text("Help clean the ocean! Collect trash, avoid fish!", text_font, (0,0,0), 100, 150)
        start_button.draw()
    elif fortnite == 0:
        print(fortnite)
        Background_ocean(background_img)
        litter_button.draw()
        fish_button.draw()
    elif fortnite == 1:
        print(fortnite)
        Background_ocean(dirty_img)
    elif fortnite == 4:
        print(fortnite)
        Background_ocean(thanks_img)

    pygame.display.update()

pygame.quit()