import pygame, sys

pygame.init()

# displays surface ((Game window)) ** Top left coordinate
screen = pygame.display.set_mode((750, 750))

pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()


# Game Loop 
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()