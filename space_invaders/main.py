import pygame, sys
from spaceship import Spaceship

pygame.init()


GREY = (29, 29, 27)

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_Group = pygame.sprite.GroupSingle()
spaceship_Group.add(spaceship)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    spaceship_Group.update()

    screen.fill(GREY)
    spaceship_Group.draw(screen)

    pygame.display.update()
    clock.tick(60)



