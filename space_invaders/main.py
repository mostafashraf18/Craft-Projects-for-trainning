import pygame, sys
from spaceship import Spaceship
from laser import Laser

pygame.init()


GREY = (29, 29, 27)

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_Group = pygame.sprite.GroupSingle()
spaceship_Group.add(spaceship)

laser = Laser((100, 100), 6, SCREEN_HEIGHT)
laser2 = Laser((100, 200), -6 , SCREEN_HEIGHT)
laser_group = pygame.sprite.Group()
laser_group.add(laser, laser2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    spaceship_Group.update()
    laser_group.update()

    screen.fill(GREY)
    spaceship_Group.draw(screen)
    laser_group.draw(screen)

    pygame.display.update()
    clock.tick(60)



