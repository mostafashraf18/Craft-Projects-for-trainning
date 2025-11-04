import pygame, sys

pygame.init()

#colors
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

# displays surface ((Game window)) ** Top left coordinate
screen = pygame.display.set_mode((750, 750))

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

