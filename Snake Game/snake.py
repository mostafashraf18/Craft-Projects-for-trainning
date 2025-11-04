import pygame, sys
from pygame.math import Vector2

pygame.init()

#colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)


## same as 750 pixels
cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
       self.position = Vector2(5,6) 
    
    def draw(self):


# displays surface ((Game window)) ** Top left coordinate
screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()


# Game Loop 
while True:

    for event in pygame.event.get():

        #exit code
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #color fill
    screen.fill(GREEN)
    # 60 frame per second 
    pygame.display.update()
    clock.tick(60)

    ## we made the canvas and the loop


    ## we now will craft an invisable grid that will help us with the movement

