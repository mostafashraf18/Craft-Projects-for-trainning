import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_Width = screen_width
        self.screen_Height = screen_height
        self.image = pygame.image.load("Graphics\spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_Width/2, self.screen_Height))
        self.speed = 6
        self.laser_group = pygame.sprite.Group()

    
    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] :
            self.rect.x += self.speed
        
        if keys[pygame.K_LEFT] :
            self.rect.x -= self.speed
        
        if keys[pygame.K_SPACE] :
            laser = Laser(self.rect.center, 5, self.screen_Height)
            self.laser_group.add(laser)
        
    def update(self):
        self.get_user_input()
        self.constrain_window()
        self.laser_group.update()

    def constrain_window(self):
        if self.rect.right > self.screen_Width:
            self.rect.right = self.screen_Width
        
        if self.rect.left < 0:
            self.rect.left = 0
        