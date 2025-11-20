import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_Width = screen_width
        self.screen_Height = screen_height
        self.image = pygame.image.load("Graphics\spaceship.png")
        self.rect = self.image.get_rect(midbottom = (self.screen_Width/2, self.screen_Height))