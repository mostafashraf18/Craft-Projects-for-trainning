import pygame, sys, random
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

        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)
    #generate random position to the food
    def generate_random_pos(self):
        x = random.randint(0, number_of_cells -1)
        y = random.randint(0, number_of_cells -1)
        position = Vector2(x, y)
        return position    

#snake class
class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5,9), Vector2(4,9)]
    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x*cell_size, segment.y*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)


# displays surface ((Game window)) ** Top left coordinate
screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()
#object from class food 
food = Food()

snake = Snake()

food_surface = pygame.image.load("Graphics/food.png")
# Game Loop 
while True:

    for event in pygame.event.get():

        #exit code
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #color fill
    screen.fill(GREEN)

    #Drawing 
    food.draw()
    snake.draw()


    # 60 frame per second 
    pygame.display.update()
    clock.tick(60)

    ## we made the canvas and the loop


    ## we now will craft an invisable grid that will help us with the movement

