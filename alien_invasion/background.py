import pygame


class Background:
    def __init__(self, location):
        self.image = pygame.image.load("images/space1.jpg")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
